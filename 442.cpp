class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
    set<int> s;
    vector<int> ans;
    for(vector<int>::iterator it=nums.begin();it!=nums.end();it++)
    {
        if(s.count(*it)==1)
            ans.push_back(*it);
        else
            s.insert(*it);
    }
    return ans;
    }
};
