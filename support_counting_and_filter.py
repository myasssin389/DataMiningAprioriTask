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

def filter_frequent(candidate_itemset_support_dict, min_support):
    filtered_candidate_itemset_support_dict = {}
    for candidate, support in candidate_itemset_support_dict.items():
        if support < min_support:
            continue
        filtered_candidate_itemset_support_dict[candidate] = support
    return filtered_candidate_itemset_support_dict