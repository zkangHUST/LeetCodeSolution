int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int cnt=0,max = 0,i=0;
    while(i<numsSize){
        if(nums[i]==1)
            cnt++;
        else{
            if(cnt>max){
                max = cnt;
            }
            cnt = 0;
        }
        i++;
    }
    if(cnt>max)
        max = cnt;
    return max;
}
