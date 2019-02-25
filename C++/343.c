int integerBreak(int n) {
    int max = 1;
    if(n==2)    
        return 1;
    else if(n==3) 
        return 2;
    while(n>4){
        max = max * 3;
        n-=3;
    }
    return max * n;
}
