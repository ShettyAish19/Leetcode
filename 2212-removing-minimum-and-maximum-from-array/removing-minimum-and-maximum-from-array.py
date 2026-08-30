class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 1

        elif n==2:
            return 2

        maxi_ind=0
        maxi=float('-inf')
        mini_ind=0
        mini=float('inf')
        leftmax=False
        leftmin=False
        rightmax=False
        rightmin=False

        for i in range(n):
            if nums[i]>maxi:
                maxi=nums[i]
                maxi_ind=i

            if nums[i]<mini:
                mini=nums[i]
                mini_ind=i
        print(maxi_ind,mini_ind)
        
    


        return min(max(maxi_ind+1,mini_ind+1),max(n-maxi_ind,n-mini_ind),maxi_ind+1+n-mini_ind,n-maxi_ind+mini_ind+1)


            


        



            
        


        