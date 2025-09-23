class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest=0
        for i,num in enumerate(nums):
            if i>farthest:
                return False
            farthest=max(i+num,farthest)

        return True


            

        