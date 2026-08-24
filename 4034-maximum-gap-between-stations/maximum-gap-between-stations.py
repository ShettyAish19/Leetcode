class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n=len(skill)
        m=len(station)
        left=[-1]*n

        right=[-1]*n
        i=0
        for j in range(m):
            if skill[i]==station[j]:
                left[i]=j
                i+=1

            if i==n:
                break

        i=n-1
        for j in range(m-1,-1,-1):
            if skill[i]==station[j]:
                right[i]=j
                i-=1

            if i<0:
                break

        ans=0
        for i in range(1,n):
            ans=max(ans,right[i]-left[i-1])

        return ans




        for i in range(len(left)):
            ans+=(right[i]-left[i-1])




        