class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total_s=sum(nums)
        n=len(nums)
        if (target+total_s)%2!=0 or abs(target)>total_s:
            return 0
        
        tar=(target+total_s)//2

        dp=[0]*(tar+1)

        dp[0]=1

        for num in nums:
            for j in range(tar,num-1,-1):
                dp[j]=dp[j]+dp[j-num]
        return dp[-1]


