# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def H(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0


        return 1+max(self.H(root.left),self.H(root.right))


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        if abs(self.H(root.left)-self.H(root.right))>1:
            return False

    
        return self.isBalanced(root.left) and self.isBalanced(root.right)

       



        