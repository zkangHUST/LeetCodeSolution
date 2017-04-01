int longestPalindrome(char* s) {
    int cntl[26]={0},cnth[26]={0};
    int len = strlen(s),i, sum = 0;
    bool flag=0;
    for(i=0;i<len;i++){
        if(s[i]>='a'&&s[i]<='z')
            cntl[s[i]-'a']++;
        else if(s[i]>='A'&&s[i]<='Z')
            cnth[s[i]-'A']++;
    }
    for(i=0;i<26;i++){
        if(cntl[i]%2!=0||cnth[i]%2!=0)
            flag = 1;
        sum=sum+cntl[i]/2*2+cnth[i]/2*2;
    }
    if(flag)
        sum++;
    return sum;
}
