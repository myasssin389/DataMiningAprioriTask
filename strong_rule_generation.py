from rule_generation import generate_rules
from confidence_computing import compute_confidence
from strong_rules_filter import filter_strong_rules
from lift_computing import compute_lift

def generate_strong_rules(frequent_itemsets_support_dict, min_confidence):
    rules_list = generate_rules(frequent_itemsets_support_dict)
    compute_confidence(rules_list)
    strong_rules_list = filter_strong_rules(rules_list, min_confidence)
    compute_lift(strong_rules_list)
    return strong_rules_list