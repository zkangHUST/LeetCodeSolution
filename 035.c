int searchInsert(int* nums, int numsSize, int target) {
    int i=0;
    while(nums[i]<target&&i<numsSize)
        i++;
    return i;
}
