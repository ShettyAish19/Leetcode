class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
    # Try 0, 1, 2, ..., until we've removed all
        for ops in range((n + 2) // 3 + 1):  # this covers all possible removals
            start = 3 * ops
            remaining = nums[start:]
            if len(set(remaining)) == len(remaining):  # check if distinct
                return ops
        return (n + 2) // 3  # fallback: worst case


        

        