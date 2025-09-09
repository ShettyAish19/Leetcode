from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q=deque([root])
        res=[]
        l_to_r=1
        while q:
            
            l=[]
            n=len(q)
            for i in range(n):
                node=q.popleft()
                l.append(node.val)
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if l_to_r:
                res.append(l)
            else:
                res.append(l[::-1])

            l_to_r=not l_to_r

        return res





        