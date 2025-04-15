class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        

        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n or grid[r][c]!=1:
                return

            
            grid[r][c]='v'
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)

        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    count+=1
                
        return count
        


        