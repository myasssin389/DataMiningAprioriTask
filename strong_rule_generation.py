from rule_generation import generate_rules
from filter import filter_strong_rules
from calculations import calculate_lift, calculate_confidence

def generate_strong_rules(frequent_itemsets_support_dict, min_confidence):
    rules_list = generate_rules(frequent_itemsets_support_dict)
    calculate_confidence(rules_list)
    strong_rules_list = filter_strong_rules(rules_list, min_confidence)
    calculate_lift(strong_rules_list)
    return strong_rules_list