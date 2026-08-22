class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        t=n
        while t!=0:
            d=t%10
            s+=d
            p*=d
            t=t//10
        return n%(s+p)==0
        
