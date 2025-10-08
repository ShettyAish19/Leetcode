class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n=len(nums)
        
        

        def getsum(is_max):
            left=[0]*n
            right=[0]*n
            st=[]
            for i in range(n):
                count=1
                while st and ( (st[-1][0]<nums[i]) if is_max else (st[-1][0]>nums[i])):
                    count+=(st.pop()[1])
                left[i]=count
                st.append((nums[i],count))

            st=[]
            for i in range(n-1,-1,-1):
                count=1
                while st and ((st[-1][0]<=nums[i]) if is_max else (st[-1][0]>=nums[i])):
                    count+=(st.pop()[1])
                right[i]=count
                st.append((nums[i],count))

            res=0
            for i in range(n):
                res+=nums[i]*left[i]*right[i]

            return res

        max_sum=getsum(True)
        min_sum=getsum(False)
        return max_sum-min_sum
                

        