import re
import fileinput
from tqdm.auto import tqdm


def generate_examples(filepath):

    # with open(filepath, encoding="utf-8") as f:
    with fileinput.input([filepath], encoding="utf-8") as f:

        add_space = 1
        doc_id, title, uri = None, None, None
        current_sentence, current_paragraph_sentences, text = "", [], []
        id_ = 0
        data = []
        count = 0
        for line in tqdm(f):

            line = line.strip()

            if line not in ["<p>", "<s>"]:  # skip these tags
                count = count + 1

                if line.startswith("<doc"):  # doc begin
                    doc_id = re.findall('docid="(.*?)"', line)[0]
                    title = re.findall('title="(.*?)"', line)[0]
                    uri = re.findall('uri="(.*?)"', line)[0]

                elif line == "<g/>":  # don't add space with <g/> occurrence
                    add_space = 0

                elif line == "</s>":  # end sentence
                    current_paragraph_sentences.append(current_sentence)
                    current_sentence = ""

                elif line == "</p>":  # end paragraph
                    text.extend(current_paragraph_sentences)
                    current_paragraph_sentences = []

                elif len(current_sentence) == 0:
                    current_sentence = line

                else:
                    current_sentence = (add_space * " ").join([current_sentence, line])
                    add_space = 1

                if line.strip() == "</doc>":  # doc end
                    data.append(" ".join(text) + "\n")

                    if count >= 1 << 25:
                        print("Partial Save")
                        with open("data/dump.txt", "a") as f:
                            f.writelines(data)

                        count = 0
                        data = []

                    # id_, {"doc_id": doc_id, "title": title, "uri": uri, "text": text}
                    id_ += 1
                    add_space = 1
                    doc_id, title, uri = None, None, None
                    current_sentence, current_paragraph_sentences, text = "", [], []


# def convert_datasets_into_dump(filepath):
#     from datasets import load_dataset

#     dataset = load_dataset('brwac', filepath)

#     def batch_text2txt(examples):
#         examples['']


if __name__ == "__main__":
    print("Python script to convert .vert file into dump.txt")
    filepath = "data/brwac.vert"
    generate_examples(filepath)
    print("Done!")
