class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num=set(nums)
        i=1
        while True:
            if k*i not in num:
                return k*i
            i+=1






        