class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        leftsum=[0]*len(nums)
        rightsum=[0]*len(nums)
        
        for i in range(1,len(nums)):
            leftsum[i]=nums[i-1]+leftsum[i-1]
            j=n-i-1
            rightsum[j]=rightsum[j+1]+nums[j+1]

        for i in range(n):
            ans[i]=abs(leftsum[i]-rightsum[i])

        return ans


        



        
        