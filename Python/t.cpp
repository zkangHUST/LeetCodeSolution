#include<iostream>
#include<vector>
using namespace std;
class Solution
{
public:
    int removeDuplicates(vector<int>& nums) 
    {
        int index = 0;
        if (nums.empty()) {
            return 0;
        }
        int len = nums.size();
        for(int i = 0 ; i < nums.size()-1; i++)
        {
            if(nums[i] != nums[i+1])
            {
                nums[++index] = nums[i+1];
            }
        }
       return len==0?index:index+1;
    }
};

int main()
{
    Solution s;
    vector<int> nums = {1};//2};//,44};
    // nums.push_back(5);
    cout << s.removeDuplicates(nums);

}