class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d={}
        s=[]
        
        for num in reversed(nums2):
            while s and s[-1]<=num:
                s.pop()

            if s:
                d[num]=s[-1]
            else:
                d[num]=-1

            s.append(num)

        return [d[i] for i in nums1]





        
        