class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> s;
        for(vector<int>::iterator it=nums.begin();it!=nums.end();it++)
        {
            if(s.count(*it)==1)
                return true;
            else
                s.insert(*it);
        }
        return false;
        
    }
};
