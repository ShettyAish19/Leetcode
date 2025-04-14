class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        dis = [[0 for _ in range(n)] for _ in range(m)]

        q=deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append(((i,j),0))
                    visited[i][j]=1
        dir=[(0,-1),(0,1),(1,0),(-1,0)]

        while q:
            t,i=q.popleft()
            r,c=t[0],t[1]
            dis[r][c]=i
            i+=1
            for dr,dc in dir:
                nr,nc=r+dr,c+dc
                if nr>=0 and nr<m and nc>=0 and nc<n and visited[nr][nc]==0:
                    q.append(((nr,nc),i))
                    visited[nr][nc]=1

        return dis


        