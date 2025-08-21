class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d={'a':0,'b':0,'c':0}
        n=len(s)
        start=0
        count=0
        for end in range(n):
            d[s[end]]+=1
            
            while d['a']>0 and d['b']>0 and d['c']>0:
                count+=(n-end)
                d[s[start]]-=1
                start+=1

        return count
        
        

        