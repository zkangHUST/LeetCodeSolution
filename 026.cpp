
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
    vector<int>::iterator i,j;
    j=i=nums.begin();
    if(i<nums.end())//加此判断是因为nums有可能为空
    j=i+1;
    while(j!=nums.end())
    {
        if(*j==*i)
            nums.erase(j);
        else
        {
            i=j;
            j++;
        }
    }
    return nums.size();
    }
};
