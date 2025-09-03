int orangesRotting(int** grid, int gridSize, int* gridColSize) {
    
    typedef struct{
        int x,y;
    }Pair;

    #define MAX 100

    Pair q[MAX*MAX];
    int rear=0;
    int front=0;
    int fresh =0;
    for(int i=0;i<gridSize;i++){
        for(int j=0;j<gridColSize[0];j++){
            if(grid[i][j]==2){
                q[rear].x=i;
                q[rear].y=j;
                rear++;
                
            }
            if(grid[i][j]==1){
                fresh+=1;
            }

        }
    }

    int time=0;
    int dir[4][2]={{0,-1},{-1,0},{1,0},{0,1}};

    while(front<rear && fresh>0){
        int size=rear-front;
        
        for(int j=0;j<size;j++){
            Pair point=q[front++];

        for(int i=0;i<4;i++){
            int nx=point.x+dir[i][0];
            int ny=point.y+dir[i][1];
        
        if(nx>=0 && nx<gridSize && ny>=0 && ny<gridColSize[0] && grid[nx][ny]==1){
            grid[nx][ny]=2;
            fresh--;
            q[rear].x=nx;
            q[rear].y=ny;
            rear++;
        }
    }
        }
    time++;
    }

    if(fresh>0){
        return -1;
    }
    else if(time==0){
        return 0;
    }
    else 
        return time;
}
