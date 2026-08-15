class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!="1":
                return 

            grid[i][j]="X"
            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)

        


            
        count=0
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and grid[i][j]!="X":
                    count+=1
                    dfs(i,j)

        return count

        