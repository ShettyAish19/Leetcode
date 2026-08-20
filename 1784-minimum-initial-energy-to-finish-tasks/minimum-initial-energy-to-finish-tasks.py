class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1]-x[0],reverse=True)

        ans=0
        cur=0
        for a,mini in tasks:
            if cur<mini:
                ans+=(mini-cur)
                cur=mini
            cur=cur-a

        return ans