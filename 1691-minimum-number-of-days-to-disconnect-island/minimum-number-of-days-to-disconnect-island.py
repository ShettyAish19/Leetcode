class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        def count_islands():
            count=0
            vis=set()

            def dfs(i,j):
                if i<0 or i>=n or j<0 or j>=m or grid[i][j]==0 or (i,j) in vis:
                    return 

                vis.add((i,j))

                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i,j-1)

            for r in range(n):
                for c in range(m):
                    if grid[r][c]==1 and (r,c) not in vis:
                        count+=1
                        dfs(r,c)

            return count


        if count_islands() !=1:
            return 0

        for r in range(n):
            for c in range(m):
                if grid[r][c]==1:
                    grid[r][c]=0

                    if count_islands()!=1:
                        return 1

                    grid[r][c]=1

        return 2


                    


        

           
            

        