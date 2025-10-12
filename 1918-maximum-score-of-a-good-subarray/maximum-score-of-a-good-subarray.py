class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left=right=k
        n=len(nums)
        cur_min=nums[k]
        maxi=nums[k]
        while left>0 or right<n-1:
            if left==0:
                right+=1

            elif right==n-1:
                left-=1

            elif nums[left-1]<nums[right+1]:
                right+=1

            else:
                left-=1

            cur_min=min(cur_min,nums[left],nums[right])
            maxi=max(maxi,cur_min*(right-left+1))

        return maxi

            

        