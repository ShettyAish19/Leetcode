class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''def f(i,buy):
            if i==n:
                return 0
            if dp[i][buy]!=-1:
                return dp[i][buy]

            if buy==1:
                dp[i][buy]=max( f(i+1,0)-prices[i],f(i+1,1))

            if buy==0:
                dp[i][buy]=max(f(i+1,1)+prices[i],f(i+1,0))

            return dp[i][buy]

            
        n=len(prices)
        dp=[[-1]*2 for _ in range(n)]
        return f(0,1)'''

        n=len(prices)
        profit=0
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]

        return profit





        