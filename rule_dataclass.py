from dataclasses import dataclass
from typing import FrozenSet, Optional

"""
Rule = A -> B
"""

@dataclass
class Rule:
    A: FrozenSet[str]
    B: FrozenSet[str]
    support_A_U_B: int
    support_A: int
    support_B: int
    confidence: Optional[float] = None
    lift: Optional[float] = None
