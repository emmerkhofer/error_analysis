Error Analysis for Paraphrase Identification 
---------------------------------------------

This project examines a paraphrase system's most confident misclassifications.

Data is from the [STS benchmark](http://ixa2.si.ehu.es/stswiki/index.php/STSbenchmark).

Instructor repository at <https://github.com/emmerkhofer/error_analysis> . 

## dev_predictions.tsv

TSV file containing system output from a logistic regression trained on the "training" segment of STS.
The logistic regression used five string similarity metrics and two vector space similarities as features.

## lab.py

`most_confident.py` prints the system prediction and original texts for the ten most confident false positives.

Example usage:

`python most_confident.py`