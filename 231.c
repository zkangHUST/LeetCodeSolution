bool isPowerOfTwo(int n) {
    if(n<=0)
        return false;
    while(n)
    {
        if(n%2!=0&&n!=1){
            return false;
        }
        n/=2;
    }
    return true;
}
