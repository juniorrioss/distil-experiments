import fileinput
from tqdm.auto import tqdm

count = 0
with open("data/minor_dump.txt", "a") as new_f:
    max_length = 1 << 12
    for i, lines in enumerate(
        tqdm(fileinput.input(["data/dump.txt"]), maxinterval=max_length)
    ):
        count = count + 1

        new_f.write(lines)
        if count >= max_length:
            fileinput.close()
            break
