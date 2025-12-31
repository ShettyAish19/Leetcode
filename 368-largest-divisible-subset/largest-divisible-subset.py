class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dp=[1]*n
        parent=[0]*n

        for i in range(n):
            parent[i]=i
        nums.sort()

        maxi=1
        index=0
        for i in range(n):
            for prev in range(i):
                if nums[i]%nums[prev]==0:
                    if dp[i]<dp[prev]+1:
                        dp[i]=dp[prev]+1

                        parent[i]=prev

            if maxi<dp[i]:
                maxi=dp[i]
                index=i

        l=[]
        while parent[index]!=index:
            l.append(nums[index])
            index=parent[index]

        l.append(nums[index])
        l.reverse()
        return l

            
        