int hammingDistance(int x, int y) {
    int temp;
    if(x<y)
    {
        temp = x;
        x = y;
        y = temp;
    }
    temp = 0;
    while(x)
    {
        if(x%2!=y%2)
            temp++;
        x/=2,y/=2;
    }
    return temp;
}
