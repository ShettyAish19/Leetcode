class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def merge(nums,low,mid,high):
            left=low
            temp=[]
            right=mid+1
            while low<=mid and right<=high:
                if nums[low]<=nums[right]:
                    temp.append(nums[low])
                    low+=1

                else:
                    temp.append(nums[right])
                    right+=1

            while low<=mid:
                temp.append(nums[low])
                low+=1

            while right<=high:
                temp.append(nums[right])
                right+=1
            for i in range(left,high+1):
                nums[i]=temp[i-left]


        def count(nums,low,mid,high):
            cnt=0
            right=mid+1
            for i in range(low,mid+1):
                while right<=high and nums[i]> 2*nums[right]:
                    right+=1

                cnt+=(right-(mid+1))
            return cnt


        def mergesort(nums,left,right):
            cnt=0
            if left>=right:
                return 0
            mid=(left+right)//2
            cnt+=mergesort(nums,left,mid)
            cnt+=mergesort(nums,mid+1,right)
            cnt+=count(nums,left,mid,right)

            merge(nums,left,mid,right)
            return cnt


        return mergesort(nums,0,len(nums)-1)

            


        