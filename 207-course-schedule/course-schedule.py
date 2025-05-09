class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for i in range(numCourses)]
        for i in prerequisites:
            adj[i[1]].append(i[0])

        vis=[0]*numCourses
        
        has_cycle=False

        def dfs(node,vis,adj):
            nonlocal has_cycle
            if vis[node]==1:
                has_cycle=True
                return

            if vis[node]==2:
                return

            vis[node]=1
            for neighbour in adj[node]:
    
                dfs(neighbour,vis,adj)

            vis[node]=2
            

        for i in range(numCourses):
            if not vis[i]:
                dfs(i,vis,adj)

        if has_cycle: 
            return False

        else:
            return True


        

        
        