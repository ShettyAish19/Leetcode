class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        pos=[]
        neg=[]
        for i in range(n):
            if nums[i]>0:
                pos.append(nums[i])

            else:
                neg.append(nums[i])

        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])

        return ans


        
        