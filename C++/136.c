int singleNumber(int* nums, int numsSize) {
    int i = 0;
    int sigle = nums[0];
    for(i=1;i<numsSize;i++)
    {
        sigle = sigle ^ nums[i];
    }
    return sigle;
}
