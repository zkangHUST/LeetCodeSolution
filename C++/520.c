bool detectCapitalUse(char* word) {
    char *p= word;
    int flag = 0;
    if(word[0]>='a'&&word[0]<='z')
        flag = 0;
    else if(word[0]>='A'&&word[0]<='Z')
        flag = 1;
    p++;
    int status = -1;
    while(*p!='\0')
    {
            if(*p>='A'&&*p<='Z')
            {
                if(status!=0)
                    status = 1;
                else 
                    return 0;
            }
            else if(*p>='a'&&*p<='z')
            {
                if(status != 1)
                    status = 0;
                else 
                    return 0;
            }
            p++;
    }
    if(flag==0&&status==1)
        return 0;
    else
        return 1;
}
