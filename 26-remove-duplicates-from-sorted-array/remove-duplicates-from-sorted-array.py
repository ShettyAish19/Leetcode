class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        n=len(nums)
        for i in range(1,n):
            if nums[j]!=nums[i]:
                j+=1
                nums[j]=nums[i]

        return j+1

            

        