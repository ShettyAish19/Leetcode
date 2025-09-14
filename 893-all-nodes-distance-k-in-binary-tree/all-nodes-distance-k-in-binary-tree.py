# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        par={}
        def dfs(node,parent):
            if node is None:
                return 

            par[node]=parent
            if node.left:
                dfs(node.left,node)

            if node.right:
                dfs(node.right,node)

        dfs(root,None)

        q=deque([(target,0)])
        vis={target}
        res=[]
        while q:
            node,dist=q.popleft()
            if dist==k:
                res.append(node.val)

            elif dist<k:
                for nei in (node.left,node.right,par[node]):
                    if nei and nei not in vis:
                        vis.add(nei)
                        q.append((nei,dist+1))

        return res
            


            
            
        