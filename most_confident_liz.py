# coding: utf-8
import csv
import numpy as np

sts_data = "../sts_strings/stsbenchmark/sts-dev.csv"
sts_predictions = "dev_predictions.tsv"

# make a dictionary {id_string : (text1, text2), }
# use to retrieve texts later
texts = {}

with open(sts_data, 'r') as sts_file:
    for line in sts_file:
        fields = line.strip().split("\t")
        t1 = fields[5]
        t2 = fields[6]
        id_n = fields[3]
        texts[id_n] = (t1, t2)


# load data from the tsv of system output
preds = []
gold = []
ids = []

with open(sts_predictions, 'r') as prediction_file:
    reader = csv.reader(prediction_file, delimiter="\t")
    next(reader)  # skip the header
    for line in reader:
        preds.append(float(line[3]))
        gold.append(line[2] == "True")
        ids.append(line[0])


# cast as numpy arrays to use numpy utils
preds = np.asarray(preds)
gold = np.asarray(gold)


min_preds = np.argsort(preds)
print(f"min_preds: {min_preds[:10]}")

num_to_print = 10
i = 0
for pred in min_preds:
    if gold[pred] == False:
        continue
    # get the id string at this index
    id_lookup = ids[pred]
    prediction = preds[pred]
    gold_standard = gold[pred]

    # use the id string as a key into the dataset
    text_pair = texts[id_lookup]

    print(f"id: {id_lookup}\tpredicted: {prediction:.03}, paraphrase: {gold_standard}")
    print(f"{text_pair[0]}\n{text_pair[1]}\n")
    i += 1
    if i == num_to_print:
        break

