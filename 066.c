/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    int flag = 0,i,tmp;
    digits[digitsSize-1]++;
    for(i=digitsSize-1;i>=0;i--)
    {
        tmp = digits[i] + flag;
        digits[i] = tmp % 10;
        flag = tmp/10;
    }
    *returnSize = flag==1?digitsSize+1:digitsSize;
    int* res = (int*)malloc(*returnSize*sizeof(int));
    if(flag)
    {
        res[0] = 1;
        for(i=0;i<digitsSize;i++)
            res[i+1] = digits[i];
    }
    else
    {
        for(i=0;i<digitsSize;i++)
            res[i] = digits[i];
    }
    return res;    
}
