class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n=len(words)
        words.sort(key=len)
        def ispredecessor(ind_w,prev_w):
            if len(ind_w)!=len(prev_w)+1:
                return False

            k=0
            i=j=0
            skipped=False
            while i<len(ind_w) and j<len(prev_w):
                if ind_w[i]==prev_w[j]:
                    i+=1
                    j+=1

                else:
                    if skipped:
                        return False
                    skipped=True
                    i+=1
                    

            return True

        
        maxi=1
        dp=[1]*n
        for ind in range(n):
            for prev in range(ind):
                if ispredecessor(words[ind],words[prev]):
                    dp[ind]=max(dp[ind],dp[prev]+1)

            maxi=max(maxi,dp[ind])

        return maxi


        