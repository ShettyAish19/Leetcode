from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0]=1
        n=len(nums)
        cur_sum=0
        count=0
        for i in range(n):
            cur_sum+=nums[i]
            count+=prefix_count[cur_sum-k]
            prefix_count[cur_sum]+=1



        return count


            
        