class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set=set(wordDict)
        dp=[False for i in range(len(s)+1)]
        dp[0]=True
        n=len(s)
        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i]= True     
                    break

        return dp[n]
        '''def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = True
        for i in range(1, n+1):
            res = False
            for w in wordDict:
                L = len(w)
                if i>=L and s[i-L:i]==w and dp[i-L]:
                    res = True
                    break
            dp[i] = res
        return dp[n]'''