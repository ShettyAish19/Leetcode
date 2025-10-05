class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''ans=[]

        for i in range(len(nums)):
            found=-1
            for j in range(1,len(nums)):
                next_ind=(i+j)%len(nums)
                if nums[next_ind]>nums[i]:
                    found=nums[next_ind]
                    break

            ans.append(found)

        return ans'''

        n=len(nums)
        ans=[-1]*n
        s=[]

        for i in range(2*n):
            num=nums[i%n]
            while s and nums[s[-1]]<num:
                ans[s.pop()]=num

            if i<n:
                s.append(i)

        return ans



