# returns dict {candidate(frozenset): support(int)}
def count_support(candidate_itemset_list, transactions_list):
    candidate_support_dict = {candidate: 0 for candidate in candidate_itemset_list}
    for transaction in transactions_list:
        for candidate in candidate_itemset_list:
            if candidate.issubset(transaction):
                candidate_support_dict[candidate] += 1
    return candidate_support_dict

# returns dict {candidate(frozenset): support(int)} where support > min_support
def filter_frequent(candidate_itemset_support_dict, min_support):
    filtered_candidate_itemset_support_dict = {}
    for candidate, support in candidate_itemset_support_dict.items():
        if support < min_support:
            continue
        filtered_candidate_itemset_support_dict[candidate] = support
    return filtered_candidate_itemset_support_dict