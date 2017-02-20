int lengthOfLastWord(char* s) {
    int count = 0;
    int i=strlen(s)-1;
    while(s[i]==' ')
        i--;
    while(s[i]!=' '&&i>=0)
        {
            count++;
            i--;
        }
        return count;
}
