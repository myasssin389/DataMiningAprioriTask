from dataclasses import dataclass
from typing import FrozenSet, Optional
from frozenset_formatter import get_formatted_frozenset

@dataclass
class Rule:
    A: FrozenSet[str]
    B: FrozenSet[str]
    support_A_U_B: int
    support_A: int
    support_B: int
    confidence: Optional[float] = None
    lift: Optional[float] = None

    def print_rule(self):
        A = get_formatted_frozenset(self.A)
        B = get_formatted_frozenset(self.B)
        print("Rule: ", A, " -> ", B)
        if self.confidence is not None:
            print("Confidence = ", self.confidence)
        if self.lift is not None:
            print("Lift = ", self.lift)
