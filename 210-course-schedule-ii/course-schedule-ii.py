class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)

        vis=[0 for i in range(numCourses)]
        has_cycle=False
        st=[]

        def dfs(node,graph,vis,st):
            nonlocal has_cycle
            if vis[node]==1:
                has_cycle=True
                return

            if vis[node]==2:
                return 

            vis[node]=1
            for i in graph[node]:
                dfs(i,graph,vis,st)

            vis[node]=2
            st.append(node)


        for i in range(numCourses):
            if vis[i]==0:
                dfs(i,graph,vis,st)

        if has_cycle:
            return []

        else:
            return st[::-1]

            

        
        