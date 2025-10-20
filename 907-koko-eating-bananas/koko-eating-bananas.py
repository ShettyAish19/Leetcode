class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_possible(a,m,h):
            hours=0
            for pile in piles:
                hours+=(pile+m-1)//m  #ceil 

            return hours<=h


        low,high=1,max(piles)
        while low<high:
            mid=(low+high)//2
            if is_possible(piles,mid,h):
                high=mid

            else:
                low=mid+1

        return low



        