int islandPerimeter(int** grid, int gridRowSize, int gridColSize) {
    int i,j,sum=0;
    for(i=0;i<gridRowSize;i++)
        for(j=0;j<gridColSize;j++)
        {
            if(grid[i][j]==1)
            {
                if(i==0||grid[i-1][j]==0)
                    sum++;
                if(i==gridRowSize-1||grid[i+1][j]==0)
                    sum++;
                if(j==0||grid[i][j-1]==0)
                    sum++;
                if(j==gridColSize-1||grid[i][j+1]==0)
                    sum++;
            }
        }
    return sum;
}
