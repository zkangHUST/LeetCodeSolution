int titleToNumber(char* s) {
    int len = strlen(s),sum = 0,i=0;
    while(i<len){
        sum = sum*26 + s[i]-'A'+1;
        i++;
    }
    return sum;
}
