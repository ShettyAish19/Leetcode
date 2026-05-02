class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
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
        dp=[[[-1]*2 for _ in range(k+1)] for _ in range(n)]
        return f(0,k,1)'''

        n=len(prices)

        s=0
        if k>=n//2:
            for i in range(1,n):
                if prices[i]-prices[i-1]>=0:
                    s+=(prices[i]-prices[i-1])

            return s

        buy=[float('-inf')]*k
        sell=[0]*k

        for price in prices:
            for i in range(k):
                if i==0:
                    buy[i]=max(buy[i],-price)
                else:
                    buy[i]=max(buy[i],sell[i-1]-price)

                sell[i]=max(sell[i],price+buy[i])

        return sell[k-1]


        