int myAtoi(char* str) {
    char *p = str;
    int flag = 1;
    while(*p==' ')
        p++;
    if(*p=='-'||*p=='+')
    {
        flag = 1-2*(*p=='-');
        p++;
    }
    int sum = 0;
    while(*p>='0'&&*p<='9')
    {
        if(sum>INT_MAX/10||(sum==INT_MAX/10&&*p-'0'>7))
        {
            if(flag==-1)    return INT_MIN;
            else        return INT_MAX;
        }
        sum = sum *10 +*p-'0';
        p++;
    }
    return sum*flag;
}
