from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k!=0:
            return False
        f=Counter(nums)

        i=0
        for num in sorted(f.keys()):
            while f[num]:
                for i in range(k):
                    if f[num+i]<=0:
                        return False

                    f[num+i]-=1

        return True

        

            
        

        