int* constructRectangle(int area, int* returnSize) {
    int *r = (int*)malloc(sizeof(int)*2);
    int i,min= area-1,diff=0;
    for(i=(int)sqrt(area);i<=area;i++)
    {
        if(area%i==0)
        {
            diff = i-area/i;
            if(diff>=0&&diff<=min)
            {
                min = diff;
                r[0] = i;
                r[1] = area/i; 
            }
            else if(diff > min)
                break;
        }
    }
    *returnSize = 2;
    return r;
}
