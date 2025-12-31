
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''dp=[]
        def binsearch(dp,x):
            l=0
            r=len(dp)
            while l<r:
                
                mid=(l+r)//2
                if x==dp[mid]:
                    return mid

                if x>dp[mid]:
                    l=mid+1

                else:
                    r=mid
            return l
            
        for num in nums:
            pos=binsearch(dp,num)
            if pos==len(dp):
                dp.append(num)
            else:
                dp[pos]=num


        return len(dp)'''

        n=len(nums)
        dp=[1]*n
        maxi=0
        for ind in range(n):
            for prev in range(ind):
                if nums[ind]>nums[prev]:
                    dp[ind]=max(dp[ind],dp[prev]+1)

            maxi=max(maxi,dp[ind])

        return maxi

            

