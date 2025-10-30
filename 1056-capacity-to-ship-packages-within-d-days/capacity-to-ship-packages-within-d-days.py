class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def possible(weights,capa):
            d=1
            n=len(weights)
            cur_load=0
            for w in weights:
                if cur_load+w<=capa:
                    cur_load+=w

                else:
                    d+=1
                    cur_load=w

                if d>days:
                    return False

            return True




                

        low=max(weights)
        high=sum(weights)

        res=-1
        while low<=high:
            mid=(low+high)//2
            if possible(weights,mid):
                res=mid  
                high=mid-1

            else:
                low=mid+1

        return res

          

               