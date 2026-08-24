class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1=len(p)
        n2=len(s)
        dp=[[-1]*n2 for _ in range(n1)]

        def isallstar(ind):
            for i in range(ind,-1,-1):
                if p[i]!='*':
                    return False

            return True

        def f(i,j):
            if i<0 and j<0:
                return True

            if i<0 and j>=0:
                return False

            if j<0:
                return isallstar(i)
            if dp[i][j]!=-1:
                return dp[i][j]

            if p[i]==s[j] or p[i]=='?':
                dp[i][j]=f(i-1,j-1)
                return dp[i][j]

            if p[i]=='*':
                dp[i][j]=f(i-1,j) or f(i,j-1)
                return dp[i][j]

            dp[i][j]= False
            return dp[i][j]


        return f(n1-1,n2-1)

            
        

        