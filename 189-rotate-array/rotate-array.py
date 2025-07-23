class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        def rev(arr,start,end):
            while start<end:
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
            return arr

        rev(nums,0,len(nums)-1)
        rev(nums,0,k-1)
        rev(nums,k,len(nums)-1)

        
