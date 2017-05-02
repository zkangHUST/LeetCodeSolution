class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
    set<int> s;
    vector<int> ans;
    int len = nums.size();
    for(vector<int>::iterator it = nums.begin();it!=nums.end();it++)
    {
        s.insert(*it);
    }
    int i=1;
    for(set<int>::iterator it=s.begin();it!=s.end();it++)
    {
        if(*it!=i)
        {
            for(;i<*it;i++)
                ans.push_back(i);
        }
        i++;
    }
    for(;i<=len;i++)
        ans.push_back(i);
    return ans;
    
    }
};
