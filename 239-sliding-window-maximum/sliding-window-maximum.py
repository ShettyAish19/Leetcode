class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''n=len(nums)
        left=0
        right=k
        ans=[]
        while  right<n+1:
            l=nums[left:right]
            maxi=max(l)
            ans.append(maxi)
            left+=1
            right+=1

        return ans'''
        ans=[]
        n=len(nums)
        q=deque()

        for i,num in enumerate(nums):
            while q and nums[q[-1]]<num:
                q.pop()

            q.append(i)

            if q[0]<=i-k:
                q.popleft()

            if i>=k-1:
                ans.append(nums[q[0]])

        return ans



        