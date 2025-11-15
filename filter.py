def filter_frequent_itemsets(candidate_itemset_support_dict, min_support):
    filtered_candidate_itemset_support_dict = {}
    for candidate, support in candidate_itemset_support_dict.items():
        if support < min_support:
            continue
        filtered_candidate_itemset_support_dict[candidate] = support
    return filtered_candidate_itemset_support_dict

def filter_strong_rules(rules_list, min_confidence):
    strong_rules_list = []
    for rule in rules_list:
        if rule.confidence >= min_confidence:
            strong_rules_list.append(rule)
    return strong_rules_list