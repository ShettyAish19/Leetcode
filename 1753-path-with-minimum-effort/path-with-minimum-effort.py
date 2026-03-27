import heapq
from collections import deque
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        '''mini=float('inf')
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
                        heapq.heappush(hp,(new_eff,nx,ny))'''

        rows = len(heights)
        cols = len(heights[0])

        def canreach(max_effort):
            q = deque([(0, 0)])
            vis = [[False]*cols for _ in range(rows)]
            vis[0][0] = True

            while q:
                x, y = q.popleft()

                if x == rows-1 and y == cols-1:
                    return True

                for dx, dy in [(-1,0),(0,-1),(1,0),(0,1)]:
                    nx, ny = x+dx, y+dy

                    if 0 <= nx < rows and 0 <= ny < cols and not vis[nx][ny]:
                        if abs(heights[nx][ny] - heights[x][y]) <= max_effort:
                            vis[nx][ny] = True
                            q.append((nx, ny))

            return False

        left, right = 0, 10**6

        while left < right:
            mid = (left + right) // 2
            if canreach(mid):
                right = mid
            else:
                left = mid + 1

        return left

            

        

        