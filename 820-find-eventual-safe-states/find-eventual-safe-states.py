import queue
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj=[[] for i in range(len(graph))]
        q=queue.Queue()

        for i in range(len(graph)):
            for j in graph[i]:
                adj[j].append(i)

        indegree=[0]*len(graph)
        for i in range(len(adj)):
            for j in adj[i]:
                indegree[j]+=1

        for i in range(len(graph)):
            if indegree[i]==0:
                q.put(i)


        ans=[]
        
        while not q.empty():
            node=q.get()
            ans.append(node)
            for j in adj[node]:
                indegree[j]-=1
                if indegree[j]==0:
                    q.put(j)

            

        ans.sort()
        return ans




        