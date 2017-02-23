char* longestPalindrome(char* s) {
    bool table[1000][1000]={false};
    int i=0,j,len = strlen(s),max=0,begin=0,l;
    for(i=0;i<len;i++)
    {
        table[i][i] = true;
        max = 1;
        begin = i;
    }
    for(i=0;i<len-1;i++)
    {
        if(s[i]==s[i+1])    
        {
            table[i][i+1] = true;
            max = 2;
            begin = i;
        }
    }
    for(l = 3;l<=len;l++)
    {
        for(i=0;i<=len-l;i++)
        {
            j = i+l-1;
            if(s[i]==s[j]&&table[i+1][j-1]==true)
            {
                table[i][j]=true;
                max = l;
                begin = i;
            }
        }
    }
    char* r= (char*)malloc(sizeof(char)*(max+1));
    i=begin,j=0;
    for(i=begin;i<begin+max;i++)
    {
        r[j]=s[i];
        j++;
    }
    r[j]='\0';
    return r;
}
