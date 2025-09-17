class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        if grid[0][0]==1 or grid[n-1][m-1]==1:
            return -1
        count=0
        q=deque([((0,0),1)])
        grid[0][0]='#'
        d=[(0,-1),(-1,-1),(-1,0),(-1,+1),(0,1),(1,1),(1,0),(1,-1)]
        while q:
            for i in range(len(q)):
                (r,c),l=q.popleft()
                if r==n-1 and c==m-1:
                    return l
                for dr,dc in d:
                    nr,nc=r+dr,c+dc

                    if nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc]==0:
                        grid[nr][nc]='#'
                        q.append(((nr,nc),l+1))



        return -1


        