'''class Solution:
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
                
        return count'''

      

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()

        # Step 1: Add all boundary 1s to the queue
        for i in range(m):
            if grid[i][0] == 1:
                q.append((i, 0))
            if grid[i][n-1] == 1:
                q.append((i, n-1))
        for j in range(n):
            if grid[0][j] == 1:
                q.append((0, j))
            if grid[m-1][j] == 1:
                q.append((m-1, j))

        # Step 2: BFS and mark all reachable land from edges
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            r, c = q.popleft()
            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                grid[r][c] = 0  # Mark visited
                for dr, dc in directions:
                    q.append((r + dr, c + dc))

        # Step 3: Count remaining 1s
        return sum(grid[i][j] == 1 for i in range(m) for j in range(n))

        


        