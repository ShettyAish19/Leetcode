class Solution:
    def minOperations(self, s: str) -> int:
        mini=float('inf')
        n=len(s)
        def forward(a,b):
            return (ord(a)-ord(b))%26

        for k in range(n):
            cost=k
            rotated=s[k:]+s[:k]
            
            for i in range(n//2):
                j=n-i-1
                a=rotated[i]
                b=rotated[j]
                cost+=min(forward(a,b),forward(b,a))

            mini=min(mini,cost)

        return mini

           


        