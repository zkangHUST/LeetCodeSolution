char* reverseString(char* s) {
    int i=0,j = strlen(s)-1;
    char p;
    while(i<j)
    {
        p = s[i];
        s[i]=s[j];
        s[j] = p;
        i++,j--;
        
    }
    return s;
}
