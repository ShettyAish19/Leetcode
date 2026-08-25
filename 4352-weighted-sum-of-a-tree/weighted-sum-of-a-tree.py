class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        n=len(parent)
        depth=[-1]*n
    
        
        '''for i in range(1,n):
            d[i]=d[parent[i]]+1
            if d[i]>h:
                h=d[i]
                '''
        def getDepth(i):
            if depth[i] != -1:
                return depth[i]

            if parent[i] == -1:
                depth[i] = 1
            else:
                depth[i] = getDepth(parent[i]) + 1

            return depth[i]
        h=1
        for i in range(n):
            h=max(h,getDepth(i))

        
        res=0
        for i in range(n):
            res+=(nums[i]*(h-depth[i]+1))
        return res


        


        