class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''def f(i,k,buy):
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
        dp=[[[-1]*2 for _ in range(3)] for _ in range(n)]
        return f(0,2,1)'''

        n=len(prices)
        buy1=float('-inf')
        sell1=0
        buy2=float('-inf')
        sell2=0

        for price in prices:
            buy1=max(buy1,-price)
            sell1=max(sell1,buy1+price)
            buy2=max(buy2,sell1-price)
            sell2=max(sell2,buy2+price)

        return sell2


        