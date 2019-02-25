char findTheDifference(char* s, char* t) {
    int cnt[26]={0};
    int i=0,len = strlen(s);
    char p;
    for(i=0;i<len;i++){
        cnt[s[i]-'a']++;
        cnt[t[i]-'a']--;
    }
    cnt[t[i]-'a']--;
    for(i=0;i<26;i++){
        if(cnt[i]!=0){
            p= 'a'+i;
            break;
        }
    }
    return p;
}
