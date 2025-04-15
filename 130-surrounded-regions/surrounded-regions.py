class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return board

        rows,col=len(board),len(board[0])

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=col or board[r][c]!='O':
                return

            board[r][c]='S'

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for i in range(rows):
            dfs(i,0)
            dfs(i,col-1)
        for j in range(col):
            dfs(0,j)
            dfs(rows-1,j)

        for i in range(rows):
            for j in range(col):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='S':
                    board[i][j]='O'

                    

        