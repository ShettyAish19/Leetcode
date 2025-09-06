# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''if root==None:
            return []
        res=[]
        
        res+=self.inorderTraversal(root.left)
        res.append(root.val)
        res+=self.inorderTraversal(root.right)

        return res'''
     
        st=[]
        cur=root
        res=[]
        while st or cur  :
            while cur:
                st.append(cur)
                cur=cur.left

            cur=st.pop()
            res.append(cur.val)
            cur=cur.right

        return res


            



