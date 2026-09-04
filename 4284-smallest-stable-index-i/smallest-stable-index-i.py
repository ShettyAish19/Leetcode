class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        maxi=[float('-inf')]*n
        maxi[0]=nums[0]
        mini=[float('inf')]*n
        mini[n-1]=nums[n-1]
        for i in range(1,n):
            maxi[i]=max(maxi[i-1],nums[i])

        for i in range(n-2,-1,-1):
            mini[i]=min(mini[i+1],nums[i])

        for i,num in enumerate(nums):
            if maxi[i]-mini[i]<=k:
                return i

        return -1
        



            
        