# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            return TreeNode(val)
        cur=root
        prev=None
        while cur:
            prev=cur
            if val>cur.val:
                cur=cur.right

            else:
                cur=cur.left
        new=TreeNode(val)
        if prev.val>val:
            prev.left=new
        else:
            prev.right=new
    
        return root
        