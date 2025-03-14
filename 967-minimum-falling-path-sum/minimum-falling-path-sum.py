class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        '''m=len(matrix)
        dp=[[-1]*len(i) for i in matrix]
        def recur(i,j,dp):
            if j<0 or j>=m:
                return float('inf')

            if i==m-1 :
                dp[i][j]=matrix[i][j]
                return dp[i][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            down=matrix[i][j]+recur(i+1,j,dp)
            
            dleft=matrix[i][j]+recur(i+1,j-1,dp)
        
            dright=matrix[i][j]+recur(i+1,j+1,dp)

            dp[i][j]=min(down,dleft,dright)
            return dp[i][j]
        return min(recur(0, j,dp) for j in range(m))'''

        m=len(matrix)
        dp=matrix[m-1]
        for i in range(m-2,-1,-1):
            temp=dp[:]
            for j in range(m):
                down=dp[j]
                left=dp[j-1] if j>0 else float('inf')
                right=dp[j+1] if j<m-1 else float('inf')
                temp[j]=matrix[i][j]+min(down,left,right)

            dp=temp

        return min(dp)
        