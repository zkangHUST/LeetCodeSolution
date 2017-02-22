int findComplement(int num) {
    char s[33];
    int i=0,sum = 0;
    while(num)
    {
        s[i]=(num%2)>0?'0':'1';
        i++;
        num/=2;
    }
    i--;
    while(i>=0)
    {
        sum = sum * 2 +s[i]-'0';
        i--;
    }
    return sum ;
}
