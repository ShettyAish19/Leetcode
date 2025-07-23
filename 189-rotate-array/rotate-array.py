class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        start=0
        count=0
        while count<n:
            cur=start
            prev=nums[start]
            while True:
                next_idx=(cur+k)%n
                nums[next_idx],prev=prev,nums[next_idx]
                cur=next_idx
                count+=1
                if cur==start:
                    break
            start+=1
            

        
