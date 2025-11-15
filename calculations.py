def calculate_confidence(rules_list):
    for rule in rules_list:
        rule.confidence = rule.support_A_U_B / rule.support_A

def calculate_lift(rules_list):
    for rule in rules_list:
        rule.lift = rule.confidence / rule.support_B

def count_support(candidate_itemset_list, transactions_list):
    candidate_support_dict = {candidate: 0 for candidate in candidate_itemset_list}
    for candidate in candidate_itemset_list:
        candidate_support_dict[candidate] = count_support_for_itemset(candidate, transactions_list)
    return candidate_support_dict

def count_support_for_itemset(candidate_itemset, transactions_list):
    support = 0
    for transaction in transactions_list:
        if candidate_itemset.issubset(transaction):
            support += 1
    return support