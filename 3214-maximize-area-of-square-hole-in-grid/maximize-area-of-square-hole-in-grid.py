class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        maxh=1
        maxv=1
        counth=1
        countv=1
        for i in range(1,len(hBars)):
            if hBars[i]-hBars[i-1]==1:
                counth+=1

            else:
                counth=1

            maxh=max(maxh,counth)

        for i in range(1,len(vBars)):
            if vBars[i]-vBars[i-1]==1:
                countv+=1

            else:
                countv=1

            maxv=max(maxv,countv)

        return min(maxh+1,maxv+1)**2

        

            
        