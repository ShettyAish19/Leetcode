class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        n=len(nums)
        count=0
        for i in range(n):
            if nums[i]==1:
                count+=1
                maxi=max(maxi,count)

            else:
                count=0

        return maxi


        