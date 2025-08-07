class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,h=0,len(nums)-1
        while(l<h):
            mid=(l+h)//2
            if mid%2==1:
                mid-=1
            if nums[mid]==nums[mid+1]:
                l=mid+2
            
            else:
                h=mid-1
        return nums[l]



        