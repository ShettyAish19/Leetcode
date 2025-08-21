from collections import defaultdict
class Solution:
  
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n=len(nums)
        def helper(nums,k):
            d=defaultdict(int)
            left=0
            maxi=0
            count=0
            for right in range(n):
                d[nums[right]]+=1

                while len(d)>k:
                    d[nums[left]]-=1
                    if d[nums[left]]==0:
                        del d[nums[left]]

                    left+=1

                count+=(right-left+1)

            return count

        return helper(nums,k)-helper(nums,k-1)
        
        