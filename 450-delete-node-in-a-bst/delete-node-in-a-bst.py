# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Found the node to delete
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Node with two children
            # Find inorder successor (smallest in right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left
            
            # Replace value with successor's
            root.val = successor.val
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, successor.val)

        return root


        