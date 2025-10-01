# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.temp=-1
        self.inorder=[]

        def in_traversal(node):
            if node is None:
                return 

            in_traversal(node.left)
            self.inorder.append(node.val)
            in_traversal(node.right)

        in_traversal(root)
        

    def next(self) -> int:
        self.temp += 1
        return self.inorder[self.temp]

        

    def hasNext(self) -> bool:
        return self.temp+1<len(self.inorder)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()