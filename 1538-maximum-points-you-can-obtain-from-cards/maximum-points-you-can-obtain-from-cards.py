class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''n=len(cardPoints)
        left=0
        right=n-k-1
        maxi=0
        s=sum(cardPoints)
        while right<n:
        
            maxi=max(maxi,s-sum(cardPoints[left:right+1]))
            left+=1
            right+=1

        return maxi'''

        ls=0
        for i in range(k):
            ls+=cardPoints[i]

        maxi=ls

        rs=0
        r=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            ls-=cardPoints[i]
            rs+=cardPoints[r]

            r-=1;
            maxi=max(maxi,ls+rs)

        return maxi




        