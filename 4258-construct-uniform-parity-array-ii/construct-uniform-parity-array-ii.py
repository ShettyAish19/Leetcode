class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        iseven=True
        for num in nums1:
            if num%2!=0:
                iseven=False
                break

        if iseven:
            return True
        if min(nums1)%2==1:
            return True

        else:
            return False

        


        
        