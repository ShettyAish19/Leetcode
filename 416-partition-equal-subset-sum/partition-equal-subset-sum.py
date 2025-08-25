class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2!=0:
            return False

        def f(ind,target):
            if target==0:
                return True

            if ind==0:
                return nums[0]==target
            
            if dp[ind][target]!=-1:
                return dp[ind][target]

            not_take=f(ind-1,target)
            take=False
            if target>=nums[ind]:
                take=f(ind-1,target-nums[ind])

            dp[ind][target]=take or not_take
            return dp[ind][target]

        n=len(nums)
        dp=[[-1]*((s//2)+1) for i in range(n)]
        return f(n-1,s//2)

            

        