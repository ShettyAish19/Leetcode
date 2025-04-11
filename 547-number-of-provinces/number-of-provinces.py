class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        count =0
        n=len(isConnected)
        l=[[] for i in range(n)]
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i!=j and isConnected[i][j]==1:
                    l[i].append(j)
                    l[j].append(i)

        visited=[0 for i in range(n)]
        
        def dfs(node,visited,l):
            
            visited[node]=1
            for i in l[node]:
                if not visited[i]:
                    dfs(i,visited,l)
                

        for i in range(n):
            if not visited[i]:
                count+=1
                dfs(i,visited,l)

        return count

        
        