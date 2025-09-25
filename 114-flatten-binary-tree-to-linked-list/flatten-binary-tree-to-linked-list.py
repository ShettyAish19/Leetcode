# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return 

        res=[]
        def preorder(node):
            if node is None:
                return []

            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        root.left=None
        
        cur=root
        for i in range(1,len(res)):

            right=TreeNode(res[i])
            cur.right=right
            cur.left=None
            cur=cur.right

        
            
        