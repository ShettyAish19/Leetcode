from functools import lru_cache
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:

        NEG = float('-inf')

    # f(n, k, state)
        next_dp = [[0, NEG, NEG] for _ in range(k + 1)]

        for price in reversed(prices):

            curr = [[0, NEG, NEG] for _ in range(k + 1)]

            for transactions in range(1, k + 1):

            # state = 0 : nothing
                curr[transactions][0] = max(
                next_dp[transactions][0],
                next_dp[transactions][1] - price,
                next_dp[transactions][2] + price
                )

            # state = 1 : long
                curr[transactions][1] = max(
                next_dp[transactions][1],
                next_dp[transactions - 1][0] + price
                )

            # state = 2 : short
                curr[transactions][2] = max(
                next_dp[transactions][2],
                next_dp[transactions - 1][0] - price
                )

            next_dp = curr

        return next_dp[k][0]







    '''def maximumProfit(self, prices: List[int], k: int) -> int:
        
        def f(i,k,state):

            if i>=n:
                return 0 if state == 0 else -float('inf')

            if k==0:
                if state==0:
                    return 0

                else:
                    return -float('inf')

            if dp[i][k][state]!=-1:
                return dp[i][k][state]
            if state==0:
                dp[i][k][state]=max(f(i+1,k,state), f(i+1,k,1)-prices[i],f(i+1,k,2)+prices[i])

            elif state==1:
                dp[i][k][state]=max(f(i+1,k,state),f(i+1,k-1,0)+prices[i])

            else:
                dp[i][k][state]=max(f(i+1,k,state),f(i+1,k-1,0)-prices[i])

            return dp[i][k][state]
        n=len(prices)
        dp=[[[-1]*3 for _ in range(k+1)] for _ in range(n+1)]
        return f(0,k,0)'''

