class Solution:
    def jump(self, nums: List[int]) -> int:
        far=0
        end=0
        jumps=0
        for i in range(len(nums)-1):
            far=max(far,i+nums[i])
            if end==i:
                jumps+=1
                end=far

        return jumps

        