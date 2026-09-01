class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m=len(classroom)
        n=len(classroom[0])

        vis=set()
        q=deque()
        litter_idx={}
        sr=0
        sc=0
        idx=0

        for i in range(m):
            for j in range(n):
                if classroom[i][j]=='S':
                    sr=i
                    sc=j

                elif classroom[i][j]=='L':
                    litter_idx[(i,j)]=idx
                    idx=idx+1

        if idx==0:
            return 0

        total=(1<<idx)-1
        q.append((sr,sc,energy,0,0))
        vis.add((sr,sc,energy,0))
        d=[(-1,0),(0,-1),(1,0),(0,1)]
        while q:
            r,c,e,mask,steps=q.popleft()

            for dr,dc in d:
                nr=r+dr
                nc=c+dc

                if nr<0 or nr>=m or nc<0 or nc>=n:
                    continue

                if classroom[nr][nc]=='X':
                    continue
                
                ne=e-1
                nmask=mask
                if ne<0:
                    continue

                if classroom[nr][nc]=='R':
                    ne=energy

                if classroom[nr][nc]=='L':
                    nmask|=(1<<litter_idx[(nr,nc)])

                if nmask==total:
                    return steps+1

                state=(nr,nc,ne,nmask)

                if state not in vis:
                    vis.add(state)
                    q.append((nr,nc,ne,nmask,steps+1))

        return -1   

            

                






        