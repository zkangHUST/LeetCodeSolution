bool checkPerfectNumber(int num) {
    int i,j;
    int sum =0;
    for(i=2;i<=sqrt(num);i++){
        if(num%i==0){
            j=num/i;
            sum= sum +i+j;
        }
    }
    sum++;
    if(sum==num&&num!=1)
        return true;
    else
        return false;
}
