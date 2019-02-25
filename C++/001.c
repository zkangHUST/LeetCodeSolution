/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *twoSum(int *nums, int numsSize, int target)
{
    int i = 0, j = 0;
    int a = -1, b = -1;
    int *ans;
    ans = (int *)malloc(sizeof(int) * 2); //根据题目要求，返回的数组必须用malloc定义
    // i从0开始遍历
    for (i = 0; i < numsSize - 1; i++) {
        // j从i+1开始遍历
        for (j = i + 1; j < numsSize; j++) { 
            if ((nums[i] + nums[j]) == target) {
                a = i; //找到答案，跳出单层循环
                b = j;
                break;
            }
        }
        // 答案找到，则跳出循环，后面的for不再执行
        if (a >= 0 && b >= 0) {
            break;
        }
    }
    *ans = a;
    *(ans + 1) = b;
    return ans; //返回指针
}
