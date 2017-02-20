int climbStairs(int n) {
    int TwoStep=1,OneStep=1,i,sum=0;
    if(n==1)
        sum = 1;
    for(i=2;i<=n;i++)
    {
        sum = TwoStep+OneStep;
        TwoStep = OneStep;
        OneStep= sum;
    }
    return sum;

}
