#include <iostream>
#include <assert.h>
#include <stdio.h>
#include<stdlib.h>

using namespace std;

/**
 * Return an array of arrays of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */

int **a;
int asize=0;
void init();
void init(){
    a=(int**)malloc(sizeof(int*)*500);
    for(int i=0;i<500;i++){
        a[i]=NULL;
    }
    asize=0;
}

void Swap(int *array,int i,int j);
void Swap(int *array,int i,int j)
 {
        int temp;
        temp=array[i];
        array[i]=array[j];
        array[j]=temp;
    }
 void Permutation(int *array,int arraysize,int start );
 void Permutation(int *array,int arraysize,int start )
    {
        if(start==arraysize-1)
        {
            asize++;
            a[asize-1]=(int*)malloc(sizeof(int)*arraysize);
            for(int i=0;i<arraysize;i++){
                //printf("%d,",array[i]);

            a[asize-1][i]=array[i];
            //如果已经到了数组的最后一个元素，前面的元素已经排好，输出。
            }
        }
        for(int i=start;i<=arraysize-1;i++)
        {
        //把第一个元素分别与后面的元素进行交换，递归的调用其子数组进行排序
                Swap(array,i,start);
                Permutation(array,arraysize,start+1);
                Swap(array,i,start);
        //子数组排序返回后要将第一个元素交换回来。
        //如果不交换回来会出错，比如说第一次1、2交换，第一个位置为2，子数组排序返回后如果不将1、2
        //交换回来第二次交换的时候就会将2、3交换，因此必须将1、2交换使1还是在第一个位置
        }
    }


int** permute(int* nums, int numsSize, int* returnSize);
int** permute(int* nums, int numsSize, int* returnSize) {
    init();
    //a=(int**)malloc(sizeof(int*)*500);
    Permutation(nums,numsSize,0);
    *returnSize=asize;
    return a;
}


void test_permute(){
        //构造nums
        int numSize=6;
    int *nums=(int*)malloc(sizeof(int)*numSize);
    for(int i=0;i<numSize;i++)
        nums[i]=i;
    nums[0]=6;
    nums[1]=3;
    nums[2]=2;
    nums[3]=7;
    nums[4]=4;
    nums[5]=-1;

    int rs=0;
    int **b= permute(nums,numSize,&rs);
    for(int i=0;i<rs;i++){
        printf("\n");
        for(int j=0;j<numSize;j++)
            printf("%d,",b[i][j]);
    }
}


int main()
{
   test_permute();
    return 0;
}
