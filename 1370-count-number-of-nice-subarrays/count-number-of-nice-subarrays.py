class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        def helper(nums,k):
            j,res,s=0,0,0

            for i in range(n):
                while j<n and s+(nums[j]%2)<=k:
                    s+=(nums[j]%2)
                    j+=1

                res+=(j-i)
                s-=(nums[i]%2)

            return res

        return helper(nums,k)-helper(nums,k-1)

        