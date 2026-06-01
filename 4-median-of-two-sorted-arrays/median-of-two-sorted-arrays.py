class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=len(nums1)
        m=len(nums2)
        nums3=[]
        i=0
        j=0
        while i<n and j<m:
            if nums1[i]<nums2[j]:
                nums3.append(nums1[i])
                i+=1
            
            else:
                nums3.append(nums2[j])
                j+=1

        while i<n:
            nums3.append(nums1[i])
            i+=1
        
        
        while j<m:
            nums3.append(nums2[j])
            j+=1

        N=len(nums3)

        if N%2==0:
            return (nums3[N//2]+nums3[N//2 -1 ])/2

        else:
            return nums3[N//2]

        

        
            




        