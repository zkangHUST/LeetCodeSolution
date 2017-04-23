#include<algorithm>
class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int sum = 0;
        for(vector<int>::iterator it = nums.begin();it!=nums.end();it+=2)
            sum += *it;
        return sum;
        
    }
};
