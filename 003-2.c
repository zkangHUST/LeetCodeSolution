int lengthOfLongestSubstring(char* s) {
    int index[256],i,start= -1,max = 0;
    for(i=0;i<256;i++)
        index[i] = -1;
    for(i=0;i<strlen(s);i++)
    {
        if(index[s[i]]>start)
            start = index[s[i]];
        index[s[i]] = i;
        max = max>(i-start)?max:(i-start);
    }
    return max;
}
