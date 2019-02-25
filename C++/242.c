bool isAnagram(char* s, char* t) {
    int cnt[26]={0},len = strlen(s),lent=strlen(t),i=0;
    bool flag = true;
    if(len!=lent)
        return false;
    for(i=0;i<len;i++){
        cnt[s[i]-'a']++;
        cnt[t[i]-'a']--;
    }
    for(i=0;i<26;i++){
        if(cnt[i]!=0){
            flag = false;
            break;
        }
    }
    return flag;
}
