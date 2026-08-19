class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n=len(stones)
        par=list(range(n))
        size=[1]*n

        def find(x):
            if par[x]==x:
                return x

            par[x]=find(par[x])
            return par[x]

        def union(x,y):
            a,b=find(x),find(y)

            if a==b:
                return 

            if size[b]>size[a]:
                a,b=b,a

            par[b]=a
            size[a]+=size[b]

        row={}
        col={}

        for i,(r,c) in enumerate(stones):
            if r in row:
                union(i,row[r])

            else:
                row[r]=i

            if c in col:
                union(i,col[c])

            else:
                col[c]=i

        components=len(set(find(i) for i in range(n)))
        return n-components


        




        