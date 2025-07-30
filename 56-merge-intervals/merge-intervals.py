from collections import defaultdict
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        merged=[intervals[0]]

        for cur in intervals[1:]:
            last=merged[-1]
            if cur[0]<=last[1]:
                last[1]=max(cur[1],last[1])

            else:
                merged.append(cur)

        return merged

            


        