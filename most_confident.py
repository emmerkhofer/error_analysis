# coding: utf-8
import csv
import numpy as np

"""Prints the ten most confident false negatives"""

sts_data = "../sts_strings/stsbenchmark/sts-dev.csv"
sts_predictions = "dev_predictions.tsv"

# make a dictionary {id_string : (text1, text2), }
# use to retrieve texts later
texts = {}

with open(sts_data, 'r') as sts_file:
    for line in sts_file:
        # add code to parse
        continue


# load data from the tsv of system output
preds = []
gold = []
ids = []

with open(sts_predictions, 'r') as prediction_file:
    reader = csv.reader(prediction_file, delimiter="\t")
    next(reader)  # skip the header
    for line in reader:
        # add code to parse
        continue


# cast as numpy arrays to use numpy utils
preds = np.asarray(preds)
gold = np.asarray(gold)


num_to_print = 10

# add code to print
