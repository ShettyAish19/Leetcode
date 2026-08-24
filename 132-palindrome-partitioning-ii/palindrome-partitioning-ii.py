class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        '''def ispal(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False

                i+=1
                j-=1

            return True'''
        ispal=[[False]*n for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j]:
                    if j-i<=2:
                        ispal[i][j]=True

                    else:
                        ispal[i][j]=ispal[i+1][j-1]
        
        def f(i):
            
            if i==n:
                return 0
            mini=float('inf')
            if dp[i]!=-1:
                return dp[i]

            for j in range(i,len(s)):
                if ispal[i][j]:
                    mini=min(mini,1+f(j+1))
            dp[i]=mini
            return mini
        dp=[-1]*n
        return f(0)-1

