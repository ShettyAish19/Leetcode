class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l1=0
        r1=len(nums)-1

        while l1<=r1:
            mid=(l1+r1)//2
            if nums[mid]==target:
                return True

            elif nums[l1]==nums[mid]==nums[r1]:
                l1+=1
                r1-=1
            elif nums[l1]<=nums[mid]:
                if nums[l1]<=target<nums[mid]:
                    r1=mid-1
                else:
                    l1=mid+1

            else:
                if nums[mid]<target<=nums[r1]:
                    l1=mid+1
                else:
                    r1=mid-1
        return False



            
            

           
        
        