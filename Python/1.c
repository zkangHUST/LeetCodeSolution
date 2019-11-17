#include<stdio.h>
int main()
{
    int i;
    int j = 0;
    int a[3];

    for (i = 1; i < 4; i++) {
        a[i] = i;
    }
    for (i = 0; i < 4; i++) {
        printf("%d, ", a[i]);
    }
    return 0;
}