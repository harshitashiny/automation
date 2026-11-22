from collections import Counter
from functools import reduce
import math

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        return reduce(math.gcd, Counter(deck).values()) >= 2