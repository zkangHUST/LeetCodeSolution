
#include<algorithm>
class Solution {
public:
    int missingNumber(vector<int>& nums) {
    sort(nums.begin(),nums.end());
    int i=0;
    for(vector<int>::iterator it=nums.begin();it!=nums.end();it++)
    {
        if(*it!=i)
            break;
        i++;
    }
    return i;
    }
};
