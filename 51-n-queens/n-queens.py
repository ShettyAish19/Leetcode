class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        grid=[['.']*n for i in range(n)]
        cols=set()
        diag=set()
        anti_diag=set()
        def backtrack(r):
            if r==n:
                res.append(["".join(row) for row in grid])
                return 

            for c in range(n):
                if c in cols or (r-c) in diag or (r+c) in anti_diag:
                    continue
                
                grid[r][c]="Q"
                cols.add(c)
                diag.add(r-c)
                anti_diag.add(r+c)
                backtrack(r+1)
                grid[r][c]='.'
                cols.remove(c)
                diag.remove(r-c)
                anti_diag.remove(r+c)

        backtrack(0)
        return res