"""
Function Requirements:

filter_strong_rules(...)
input: list of rules with calculated confidence, min_confidence
output: list of strong rules
"""
import pandas as pd
data=[{'1':{'d'},'2':{'m'},'c': 0.9},{'1': {'x'},'2': {'y'},'c': 0.3},{'1': {'t'},'2': {'n'},'c': 0.7}]          """  c -> conf.  """
def srs(rules, mc):  """ mc -> min conf.  ,  srs -> strong rules"""
 if isinstance(rules, pd.DataFrame):
  sr=rules[rules['c'] >= min_confidence]   """  sr -> strong rule """
  return sr.reset_index(drop=True)
 elif isinstance(rules, list):
  sr=[rule for rule in rules if rule.get('c', 0) >= mc]
  return sr
   


srf = srs(data, 0.5)      """   srf -> strong rules filtering """
print(srf)
