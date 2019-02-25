#include<stdio.h>
int test(int a);
int main()
{
    int (*pf)(int );
    pf = test;
    printf("%d\n", int(*pf)(1024));
    // printf("%d\n", (int)(*pf)(1024));
    return 0;

}

int test(int a) 
{
    return ++a;
}