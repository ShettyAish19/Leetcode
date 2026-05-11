class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        def f(i):
            
            if i==n-1:
                return 0
            if dp[i]!=-1:
                return dp[i]

            maxi=float('-inf')
            for j in range(i+1,n):
                if -target<=nums[j]-nums[i]<=target:
                    maxi=max(f(j)+1,maxi)

            dp[i]= maxi
            return dp[i]

            

        n=len(nums)
        dp=[-1]*(n)
        res=f(0)
        return res if res!=float('-inf') else -1
        