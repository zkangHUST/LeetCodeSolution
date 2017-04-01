char* convertToBase7(int num) {
    char* r= (char*)malloc(15);
    bool flag = 0;
    if(num==0){
        r[0]='0';
        return r;
    }
    else if(num<0){
        flag = 1;
        num = num*-1;
    }
    int i=1;
    while(num){
        r[i] = num%7+'0';
        num/=7;
        i++;
    }
    r[i]='\0';
    int j=i-1;
    char p;
    for(i=1;i<j;i++,j--){
        p = r[i];
        r[i]=r[j];
        r[j]=p;
    }
    if(flag){
        r[0]='-';
        return r;
    }
return r+1;
}
