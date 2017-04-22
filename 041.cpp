#include<set>
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
    set<int> s;
    for(vector<int>::iterator it=nums.begin();it!=nums.end();it++)
    {
        if(*it>0)
            s.insert(*it);
    }
    int i=1;
    for(set<int>::iterator it=s.begin();it!=s.end();it++)
    {
        if(*it!=i)
            break;
        i++;
    }
    return i;
    }
};
