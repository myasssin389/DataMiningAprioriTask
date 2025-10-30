from typing import List, Dict, FrozenSet, Iterable
from itertools import combinations
from candidate_generation import generate_pruned_candidates, generate_first_candidate_itemsets
from support_counting_and_filter import count_support, filter_frequent

def apriori(transactions_list, min_support):
    frequent_itemsets_per_level_dict = {}

    first_candidate_itemsets_list = generate_first_candidate_itemsets(transactions_list)
    first_candidate_support_dict = count_support(first_candidate_itemsets_list, transactions_list)
    prev_frequent_itemsets_dict = filter_frequent(first_candidate_support_dict, min_support)
    frequent_itemsets_per_level_dict[1] = prev_frequent_itemsets_dict

    k = 2
    while True:
        candidate_itemsets_list = generate_pruned_candidates(prev_frequent_itemsets_dict, k)
        candidate_support_dict = count_support(candidate_itemsets_list, transactions_list)
        frequent_itemsets_dict = filter_frequent(candidate_support_dict, min_support)

        if not frequent_itemsets_dict:
            break

        frequent_itemsets_per_level_dict[k] = frequent_itemsets_dict
        prev_frequent_itemsets_dict = frequent_itemsets_dict
        k += 1

    return frequent_itemsets_per_level_dict