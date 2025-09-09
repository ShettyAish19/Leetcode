# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=float('-inf')

        def path(node):
            if not node:
                return 0

            lefts=max(path(node.left),0)
            rights=max(path(node.right),0)

            self.maxi=max(self.maxi,lefts+rights+node.val)

            return max(lefts,rights)+node.val

        path(root)
        return self.maxi

        