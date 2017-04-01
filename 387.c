int firstUniqChar(char* s) 
{
    int cnt[26]={0};
    int p=-1,i,len=strlen(s);
    for(i=0;i<len;i++)
        cnt[s[i]-'a']++;
    for(i=0;i<len;i++){
        if(cnt[s[i]-'a']==1){
            p=i;
            break;
        }
    }
    return  p;
}
