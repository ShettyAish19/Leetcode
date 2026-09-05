class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def ispossible(x):
            s=0
            for i in nums:
                s+=((i+x-1)//x)

            return s<=threshold

        low=1
        high=max(nums)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if ispossible(mid):
                ans=mid
                high=mid-1

            else:
                low=mid+1

        return ans


        