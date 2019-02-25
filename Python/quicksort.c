#include<stdio.h>
int  partion(int a[], int start, int end);
void quicksort(int a[], int start, int end) ;
void swap(int* a, int* b) ;
int main()
{
    int a[] = {1,7,6,2,5,3,4,4,1,5,6};
    return 0;
}
void quicksort(int a[], int start, int end) 
{
    int index = 0;
    if(start >= end) {
        return ;
    }
    index = partion(a, start, end);
    if(start < index) {
        quicksort(a, start, index-1);
    }
    if (index < end) {
        quicksort(a, index + 1, end);
    }

}
int  partion(int a[], int start, int end) 
{
    int index = rand()%(end - start + 1) + start;
    int i = start, j = end - 1;
    swap(&a[index], &a[end]);
    while(i < j) {
        while(i < j && a[i] < a[end]) 
            i++;
        while(i < j && a[j] > a[end]) 
            j--;
        swap(&a[i], &a[j]);
    }
    if (a[i] > a[end]) {
        swap(&a[i], &a[end]);
    }
    return i;
}

void swap(int* a, int* b) 
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}