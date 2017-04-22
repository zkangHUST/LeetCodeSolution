#include<set>
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        set<int> s;
        int res;
        for(vector<int>::iterator it=nums.begin();it!=nums.end();it++)
        {
            if(s.count(*it)==0)
                s.insert(*it);
            else
            {
                res = *it;
                break;
            }
        }
        return res;
    }
};
