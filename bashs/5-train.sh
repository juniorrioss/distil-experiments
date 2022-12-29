export NODE_RANK=0
export N_NODES=1
export N_GPU_NODE=1
export MASTER_PORT=1234
export MASTER_ADDR=localhost

pkill -f 'python -u train.py'

python -m torch.distributed.launch \
    --nproc_per_node=$N_GPU_NODE \
    --nnodes=$N_NODES \
    --node_rank $NODE_RANK \
    --master_addr $MASTER_ADDR \
    --master_port $MASTER_PORT \
    train.py \
        --force \
        --n_gpu $N_GPU_NODE \
        --local_rank -1 \
        --student_type roberta \
        --student_config training_configs/distilroberta-base.json \
        --teacher_type roberta \
        --teacher_name roberta-base \
        --alpha_ce 0.33 --alpha_mlm 0.33 --alpha_cos 0.33 --alpha_clm 0.0 --mlm \
        --temperature 2.0 \
        --freeze_pos_embs \
        --dump_path serialization_dir/my_first_trainingg \
        --data_file data/binarized_text.roberta-base.pickle \
        --token_counts data/token_counts.roberta.pickle \
        --student_pretrained_weights roberta_distiled_initial_checkpoint.pth \
        --seed 56 \
        --learning_rate 5e-4 \
        --checkpoint_interval 2000 \
        --warmup_prop 0.05 \
        --weight_decay 0 \
        --gradient_accumulation_steps 20 \
        --batch_size 2
