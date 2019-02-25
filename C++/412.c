/**
*Return an array of size *returnSize.
*Note: The returned array must be malloced, assume caller calls free().
*/
char** fizzBuzz(int n, int* returnSize) 
{
    char buf[10]={0};
    *returnSize = n;
    char** r = (char**)malloc(sizeof(char*)*n);//先声明指针数组
    int i=0;
    for(i=0;i<n;i++)
    {
        if((i+1)%3==0&&(i+1)%5==0)
            strcpy(buf,"FizzBuzz");
        else if((i+1)%3==0)
            strcpy(buf,"Fizz");
        else if((i+1)%5==0)
            strcpy(buf,"Buzz");
        else
            sprintf(buf,"%d",i+1);
        r[i] = (char*)malloc(strlen(buf)+1);//分配空间
        strcpy(r[i],buf);
        buf[0]='\0';
    }
    return r;
}
