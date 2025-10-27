"""
Function Requirements:

generate_first_candidate_frozenset(...)
input: transaction list
output: frozenset of 1-itemset candidates

generate_pruned_candidates(...)
input: frozenset of (k-1)-itemsets (previous frequent itemsets), k (size)
output: frozenset of pruned candidates

HELPER FUNCTION:
prune_candidates(...)
input: frozenset of candidates, previous frozenset of frequent itemsets (k-1)-itemsets
output: frozenset of pruned candidates
pruning = if any (k-1) subset of candidate k-itemsets
        is not in L(k-1) (previous frequent itemset frozenset)
        then the candidate should be removed from the candidate k-itemsets
"""