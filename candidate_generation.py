from itertools import combinations

# returns list[frozenset] frozenset = itemset
def generate_first_candidate_itemsets(transactions_list):
    items = set()
    for transaction in transactions_list:
        for item in transaction:
            items.add(frozenset([item]))
    return list(items)

# returns list[frozenset] of pruned candidates
def generate_pruned_candidates(prev_frequent_itemset_dict, k):
    if k < 2:
        raise ValueError("k must be >= 2 for generate_pruned_candidates")

    candidate_itemset_list = []
    num_prev = len(prev_frequent_itemset_dict)
    prev_frequent_itemset_list = list(prev_frequent_itemset_dict.keys())

    for i in range(num_prev):
        for j in range(i + 1, num_prev):
            union_set = prev_frequent_itemset_list[i] | prev_frequent_itemset_list[j]

            if len(union_set) == k and union_set not in candidate_itemset_list:
                candidate_itemset_list.append(union_set)

    pruned_candidates = prune_candidates(prev_frequent_itemset_list, candidate_itemset_list)
    return pruned_candidates

def prune_candidates(prev_frequent_itemset_list, candidate_itemset_list):
    pruned_list = []
    prev_frequent_itemset_set = set(prev_frequent_itemset_list)
    for candidate in candidate_itemset_list:
        all_subsets_frequent = True
        for subset in combinations(candidate, len(candidate) - 1):
            if frozenset(subset) not in prev_frequent_itemset_set:
                all_subsets_frequent = False
                break
        if all_subsets_frequent:
            pruned_list.append(candidate)
    return pruned_list
