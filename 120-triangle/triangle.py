'''class Solution:
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
        
        return f(0,0)'''

       

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = triangle[-1][:]  # Initialize dp as the last row of the triangle

        # Bottom-up DP starting from second-last row
        for i in range(m - 2, -1, -1):
            for j in range(i + 1):  # Only iterate valid elements in the current row
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]  # The top cell now contains the minimum path sum
