class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        
        left=0
        start=0
        mini=float('inf')

        for i in range(len(s)):
            if s[i]=='1':
                k-=1

            
            while k==0:
                cur=i-left+1
                if cur<mini:
                    mini=i-left+1
                    start=left

                elif cur==mini:
                    if s[left:i+1]<s[start:start+mini]:
                        start=left


                if s[left]=='1':
                    k+=1
                left+=1
        if mini==float('inf'):
            return ""
        return s[start:start+mini]

            





        