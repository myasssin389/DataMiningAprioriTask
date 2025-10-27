"""
Function Requirements:

apriori(...)
input: transactions_list, min_support
output: dict of level: [dict of frequent itemsets (frozenset): support]

functions available to use:
generate_first_candidate_itemsets()
generate_pruned_candidates()
count_support()
filter_frequent()

see: candidate_generation.py, support_counting_and_filter.py for functions details
"""