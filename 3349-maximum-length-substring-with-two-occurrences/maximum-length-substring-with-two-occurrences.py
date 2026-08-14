class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        maxi=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                d={}
                ans=True
                for k in range(i,j+1):
                   d[s[k]]=d.get(s[k],0)+1

                for l in d.values():
                    if l>2:
                        ans=False
                        break
                if ans==True:
                    maxi=max(maxi,j-i+1)

        return maxi
                


        