class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD=10**9+7
        last_seen={}
        dp=[1]*(len(s)+1)

        for i,ch in enumerate(s):
            dp[i+1]=(dp[i]*2)%MOD
            if ch in last_seen:
                dp[i+1]=(dp[i+1]-dp[last_seen[ch]]) %MOD

            last_seen[ch]=i

        return (dp[-1]-1 )%MOD 