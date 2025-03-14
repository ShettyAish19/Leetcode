class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        m=len(triangle)
        dp=[[-1]*len(i) for i in triangle]
        def f(i,j):
            if i==m-1:
                return triangle[i][j]

            if dp[i][j]!=-1:
                return dp[i][j]
            left=triangle[i][j]+f(i+1,j)
            right=triangle[i][j]+f(i+1,j+1)
            dp[i][j]=min(left,right)
            return dp[i][j]
        
        return f(0,0)

        