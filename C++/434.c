int countSegments(char* s) {
    char* p = s;
    int status = 0,count=0;
    while(*p==' ')
        p++;
    if(*p!='\0')
        status = 1;
    while(*p!='\0')
    {
        if(*p==' '&&status==1)
        {
            status = 0;
            count++;
        }
        else if(*p!=' '&&status ==0) 
        {
            status = 1;
        }
        p++;            
    }
    if(status)
        count++;
    return count;
}
