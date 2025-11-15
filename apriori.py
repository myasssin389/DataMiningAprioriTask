from candidate_generation import generate_pruned_candidates, generate_first_candidate_itemsets
from filter import filter_frequent_itemsets
from calculations import count_support

def apriori(transactions_list, min_support):
    frequent_itemsets_support_dict = {}

    first_candidate_itemsets_list = generate_first_candidate_itemsets(transactions_list)
    first_candidate_support_dict = count_support(first_candidate_itemsets_list, transactions_list)
    prev_frequent_itemsets_dict = filter_frequent_itemsets(first_candidate_support_dict, min_support)
    frequent_itemsets_support_dict.update(prev_frequent_itemsets_dict)

    k = 2
    while True:
        candidate_itemsets_list = generate_pruned_candidates(prev_frequent_itemsets_dict, k)
        candidate_support_dict = count_support(candidate_itemsets_list, transactions_list)
        frequent_itemsets_dict = filter_frequent_itemsets(candidate_support_dict, min_support)

        if not frequent_itemsets_dict:
            break

        frequent_itemsets_support_dict.update(frequent_itemsets_dict)
        prev_frequent_itemsets_dict = frequent_itemsets_dict
        k += 1

    return frequent_itemsets_support_dict