class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def ispossible(f):
            count=1
            last_pos=position[0]

            for i in range(1,len(position)):
                if position[i]-last_pos>=f:
                    last_pos=position[i]
                    count+=1

                    if count>=m:
                        return True

            return False

        low=min(position[i+1]-position[i] for i in range(len(position)-1))
        high=max(position)-min(position)
        ans=0
        while low<=high:
            mid=(low+high)//2
            if ispossible(mid):
                ans=mid
                low=mid+1

            else:
                high=mid-1

        return ans

        