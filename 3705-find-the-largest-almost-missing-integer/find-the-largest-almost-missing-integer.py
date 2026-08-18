from collections import Counter

class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Case 1: The window size is the size of the array
        if k == n:
            return max(nums)
        
        # Count frequencies of all elements
        counts = Counter(nums)
        
        # Case 2: Each element is its own subarray
        if k == 1:
            unique_elements = [x for x in nums if counts[x] == 1]
            return max(unique_elements) if unique_elements else -1
        
        # Case 3: 1 < k < n (Only boundary elements can be almost missing)
        ans = -1
        if counts[nums[0]] == 1:
            ans = max(ans, nums[0])
        if counts[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans
         




            

                
            
        