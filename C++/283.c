void moveZeroes(int* nums, int numsSize) {
    int i,j;
    while(nums[i]!=0)
        i++;
    j=i;
    while(nums[j]==0)
        j++;
    int temp;
    while(j<numsSize)
    {
        temp = nums[i];
        nums[i]=nums[j];
        nums[j]=temp;
        j++;
        while(nums[j]==0&&j<numsSize)
            j++;
        i++;
        while(nums[i]!=0&&i<j)
            i++;
    }
}
