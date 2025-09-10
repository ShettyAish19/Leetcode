# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        q.append((root,0,0))
        nodes=[]

        while q:
            node,r,c=q.popleft()
            nodes.append((c,r,node.val))
            if node.left:
                q.append((node.left,r+1,c-1))

            if node.right:
                q.append((node.right,r+1,c+1))

        nodes.sort(key=lambda x:(x[0],x[1],x[2]))

        col_table = defaultdict(list)
        for col, row, val in nodes:
            col_table[col].append(val)

        return [col_table[x] for x in col_table.keys()]
        #return [col_table[x] for x in sorted(col_table.keys())]

            
        