class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        visited=[[0]*n for i in range(m)]
        fresh=0
        q=deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))

                elif grid[i][j]==1:
                    fresh+=1

        dir=[(-1,0),(1,0),(0,1),(0,-1)]
        if fresh ==0:
            return 0
        time=0
        while q and fresh>0:
            for k in range(len(q)):
                r,c=q.popleft()
                for dr,dc in dir:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        q.append((nr,nc))
                        fresh-=1
            time+=1

        return time if fresh==0 else -1



        