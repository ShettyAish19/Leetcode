# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi=0
        q=deque([(root,0)])
        while q:
            n=len(q)
            node,first=q[0]
            node,last=q[-1]
            maxi=max(maxi,last-first+1)

            for i in range(n):
                node,index=q.popleft()
                if node.left:
                    q.append((node.left,2*index+1))

                if node.right:
                    q.append((node.right,2*index+2))

        return maxi

            





        