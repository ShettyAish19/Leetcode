class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        
        arr1=[]
        arr2=[]

        arr1.append(nums[0])
        arr2.append(nums[1])
        op=len(nums)-2
        l1=nums[0]
        l2=nums[1]
        j=2

        for i in range(op):
            if j>=len(nums):
                break

            if l1>l2:
                arr1.append(nums[j])
                l1=nums[j]

            else:
                arr2.append(nums[j])
                l2=nums[j]

            j+=1

        return arr1+arr2

        


        