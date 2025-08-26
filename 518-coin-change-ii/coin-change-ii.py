class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[0]*(amount+1) for i in range(n+1) ]
        
        dp[0][0]=1

        for i in range(1,n+1):
            for j in range(amount+1):
                not_take=dp[i-1][j]
                take=0
                
                if j>=coins[i-1]:
                    take=dp[i][j-coins[i-1]]
                    
                dp[i][j]=take+not_take
                
        return dp[n][amount]

        