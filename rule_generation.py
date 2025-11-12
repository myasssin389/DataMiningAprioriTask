from dataclasses import dataclass
from typing import FrozenSet, Dict, List
from itertools import combinations

@dataclass
class Rule:
    A: FrozenSet[str]
    B: FrozenSet[str]
    support_A_U_B: int
    support_A: int
    support_B: int

def generate_rules(frequent_itemsets: Dict[FrozenSet[str], int]) -> List[Rule]:
    rules: List[Rule] = []

    for itemset in frequent_itemsets:
        if len(itemset) < 2:
            continue

        s = list(itemset)
        for i in range(1, len(s)):
            for combo in combinations(s, i):
                A = frozenset(combo)
                B = itemset - A
                if B in frequent_itemsets:
                    rules.append(Rule(A, B, frequent_itemsets[itemset], frequent_itemsets[A], frequent_itemsets[B]))

    return rules

