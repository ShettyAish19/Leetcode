class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def f(i,k,buy):
            if i>=n or k<=0:
                return 0
            if dp[i][k][buy] !=-1:
                return dp[i][k][buy]
            if buy==1:
                dp[i][k][buy]=max(f(i+1,k,0)-prices[i],f(i+1,k,1))

            if buy==0:
                dp[i][k][buy]= max(f(i+1,k-1,1)+prices[i],f(i+1,k,0))
            return dp[i][k][buy]

        n=len(prices)
        dp=[[[-1]*2 for _ in range(k+1)] for _ in range(n)]
        return f(0,k,1)
        