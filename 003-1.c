int lengthOfLongestSubstring(char* s) {
    int i=0,j=0,max=0,len=0;
    int cnt[256]={0};
    while(j<strlen(s))
    {
        if(cnt[s[j]]!=0)
  	{
		len = j - i;
		max = len>max?len:max;
		for(;s[i]!=s[j];i++)
           	     cnt[s[i]] = 0;
           	 cnt[s[i++]]=0;
           	 cnt[s[i]]++;
           	 cnt[s[j]]++;
           	 len = 0;
        }
        cnt[s[j]]++;
        j++;
    }
    len = j-i;
    max = len>max?len:max;
    return max;
}
