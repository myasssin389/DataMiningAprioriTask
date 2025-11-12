"""
Function Requirements:

filter_strong_rules(...)
input: list of rules with calculated confidence, min_confidence
output: list of strong rules
"""
import pandas as pd

strongrules = rules[(rules['confidence'] >= 0.6) & (rules['support'] >= min_support_val)].copy()
strongrules = strongrules.sort_values(['lift', 'confidence', 'support'], ascending=False)

col = ['support', 'confidence', 'lift']
print(strongrules[cols_to_show].head(15))
