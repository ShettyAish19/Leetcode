class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        '''def f(i,buy):
            if i>=n:
                return 0
            if dp[i][buy]!=-1:
                return dp[i][buy]

            if buy==1:
                dp[i][buy]= max(f(i+1,buy),-prices[i]+f(i+1,0))

            else:
                dp[i][buy]= max(f(i+1,buy),prices[i]+f(i+1,1)-fee)
            return dp[i][buy]
        n=len(prices)
        dp=[[-1]*2 for _ in range(n)]
        return f(0,1)'''

        sell=0
        buy=-prices[0]

        for price in prices[1:]:
            sell=max(sell,price+buy-fee)
            buy=max(buy,sell-price)

        return sell
            


        