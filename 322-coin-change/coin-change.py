class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def f(rem):
            if rem==0:
                return 0

            if rem<0:
                return float('inf')

            if rem in dp:
                return dp[rem]

            mini=float('inf')
            for c in coins:
                mini=min(mini,1+f(rem-c))

            dp[rem]=mini
            return mini

        dp={}
        res=f(amount) 
        return res if res!=float('inf') else -1
                
        