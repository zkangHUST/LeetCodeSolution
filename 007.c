int reverse(int x) {
    char s[33];
    int flag = 1,p,i=0;
    long long sum = 0;
    if(x<0)
    {
        if(x==INT_MIN)
            return 0;
        flag = -1;
        x = -x;
    }
    while(x)
    {
        p = x%10;
        s[i++] = p+'0';
        x/=10;
    }
    s[i] = '\0';
    i=0;
    while(s[i]!='\0')
    {
        sum = sum*10 + s[i] - '0';
        if(sum>INT_MAX)
        {
            sum = 0;
            break;
        }
        i++;
    }
    sum = sum * flag;
    return sum;
}
