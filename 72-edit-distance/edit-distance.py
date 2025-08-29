class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''def f(i,j):
            if i<0:
                return j+1
            if j<0:
                return i+1


            if word1[i]==word2[j]:
                op=f(i-1,j-1)

            else:
                insert=1+f(i,j-1)
                delete=1+f(i-1,j)
                replace=1+f(i-1,j-1)

                op=min(insert,delete,replace)

            return op
        n,m=len(word1),len(word2)
        return f(n-1,m-1)'''

        n,m=len(word1),len(word2)
        dp=[[0]*(m+1) for i in range(n+1)]

        for j in range(1,m+1):
            dp[0][j]=j

        for i in range(1,n+1):
            dp[i][0]=i

        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]

                else:
                    dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])

        return dp[n][m]
            

        
        