class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        '''maxi=0
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

        return maxi'''


        char_count = {}
        left = 0
        maxi = 0
        
        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            
            while char_count[s[right]] > 2:
                char_count[s[left]] -= 1
                left += 1
                
            maxi = max(maxi, right - left + 1)
            
        return maxi
                


        