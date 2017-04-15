char* reverseWords(char* s) {
    char* begin,*end,*p;
    begin=end=p=s;
    char* res = (char*)malloc(strlen(s)+1);
    char* q= res;
    char* i;
    while(*p!='\0')
    {
        if(*p==' ')
        {
            end = p;          
            for(i=end-1;i>=begin;i--)
                *q++ = *i;
            *q++=' ';
            begin=end+1;
        }
        p++;
    }
    end = p;
    for(i=end-1;i>=begin;i--)
        *q++=*i;
    *q=*p;
    return res;
}
