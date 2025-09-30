# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root=TreeNode(preorder[0])
        st=[root]
        for val in preorder[1:]:
            if val<st[-1].val:
                node=TreeNode(val)
                st[-1].left=node
                st.append(node)

            else:
                parent=None
                while st and st[-1].val<val:
                    parent=st.pop()
                node=TreeNode(val)
                parent.right=node
                st.append(node)

        return root

        