class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        def is_possible(x):
            count=0
            consecutive_flowers=0
            for i in bloomDay:
                if i<=x:
                    consecutive_flowers+=1
                    if consecutive_flowers==k:
                        count+=1
                        consecutive_flowers=0

                else:
                    consecutive_flowers=0



            return count>=m


        low=min(bloomDay)
        high=max(bloomDay)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if is_possible(mid):
                ans=mid
                high=mid-1

            else:
                low=mid+1

        return ans 

        