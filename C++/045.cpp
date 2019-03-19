class Solution {
public:
    int jump(vector<int>& nums) {
        int             cnt = 1, i = 0, j = 0, index = 0, size;

        size = nums.size();
        if (size <= 1) {
            return 0;
        }
        while (index + nums[index] < size - 1) {
            for (i = index + 1; i <= index + nums[index] && i < size; i++) {
                if (i + nums[i] > j + nums[j]) {
                    j = i;
                }
            }
            index = j;
            cnt++;
        }
        return cnt;
    }
};