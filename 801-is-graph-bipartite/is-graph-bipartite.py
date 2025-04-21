class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colour=[-1 for i in range(len(graph))]
        
        def dfs(n,col,colour,graph):
            colour[n]=col
            
            for i in graph[n]:
                if(colour[i]==-1):
                    if(dfs(i,1-col,colour,graph)==False):
                        return False


                elif colour[i]==col:
                    return False

            return True


        for i in range(len(graph)):
            if colour[i]==-1:
                if(dfs(i,0,colour,graph)==False):
                    return False

        return True


