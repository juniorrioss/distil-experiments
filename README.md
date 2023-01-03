# Distilation Repo
## Guide to use this repository

This folder contains code used from huggingface to train Distil* as well as examples showcasing how to use DistilBERT, DistilRoBERTa and DistilGPT2.


### Download Data and preprocess
```bash
  bash bashs/01-prepare_data.sh

  bash bashs/02-vert2dump.sh
```


### Download Data already processed
```bash
  bash bashs/03-download_dump.sh
```

### Tokenize Data once (depends on tokenizer)
```bash
  bash bashs/2-binarize_data.sh
```

### Frequency count on vocab (depends on vocab size from tokenizer)
```bash
  bash bashs/3-token_counts.sh
```

### Initialize distiled checkpoint (default to roberta for 6 layers)
```bash
  bash bashs/4-extract_layer.sh
```

### Train distiled student

```bash
  bash bashs/5-train.sh



  # Default parameters:
  --alpha_ce 0.33 --alpha_mlm 0.33 --alpha_cos 0.33
  --temperature 2.0 learning_rate 5e-4 --warmup_prop 0.05
  --gradient_accumulation_steps 20 --batch_size 2
```

##### Reminder: - create a .env file / - change hyperparameters for training 

