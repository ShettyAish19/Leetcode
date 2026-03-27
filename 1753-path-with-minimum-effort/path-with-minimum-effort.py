import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        mini=float('inf')
        hp=[(0,0,0)] #effort,row,column

        r=len(heights)
        c=len(heights[0])

        diri=[(-1,0),(1,0),(0,-1),(0,1)]
        effort=[[float('inf')]*c for i in range(r)]
        while hp:
            cur_eff,row,col=heapq.heappop(hp)

            if row==r-1 and col==c-1:
                return cur_eff

            for dr,dc in diri:
                nx,ny=row+dr,col+dc
                if 0<=nx<r and 0<=ny<c:
                    new_eff=max(cur_eff,abs(heights[row][col]-heights[nx][ny]))

                    if new_eff<effort[nx][ny]:
                        effort[nx][ny]=new_eff
                        heapq.heappush(hp,(new_eff,nx,ny))

            

        

        