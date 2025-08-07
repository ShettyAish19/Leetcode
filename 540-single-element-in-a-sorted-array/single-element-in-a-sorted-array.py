class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,h=0,len(nums)-1
        while(l<h):
            if nums[l]==nums[l+1]:
                l+=2
            if nums[h]==nums[h-1]:
                h-=2

        return nums[l]

        