class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        from collections import Counter
import math
from typing import List

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        MAXX = 1 << 10   # values up to 1024
        n = len(nums)
        INF = math.inf

        # Group by index % k
        groups = [[] for _ in range(k)]
        for i, v in enumerate(nums):
            groups[i % k].append(v)

        # DP array: start with "infinite cost"
        dp = [INF] * MAXX
        dp[0] = 0

        for g in groups:
            freq = Counter(g)
            size = len(g)
            ndp = [INF] * MAXX
            minPrev = min(dp)

            for x in range(MAXX):
                # Case 1: change all elements in group to something new
                ndp[x] = min(ndp[x], minPrev + size)

                # Case 2: keep some value v in this group
                for v, cnt in freq.items():
                    ndp[x] = min(ndp[x], dp[x ^ v] + (size - cnt))

            dp = ndp

        return dp[0]

        
        