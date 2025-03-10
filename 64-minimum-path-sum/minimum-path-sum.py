class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1]*n for i in range(m)]
        dp[0][0]=grid[0][0]
        def f(i,j,dp):

            if i<0 or j<0:
                return float('inf')
            if i==0 and j==0:
                return dp[i][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            s_left=grid[i][j]+f(i,j-1,dp)
            s_up=grid[i][j]+f(i-1,j,dp)
            dp[i][j]=min(s_left,s_up)
            return dp[i][j]

        return f(m-1,n-1,dp)
        