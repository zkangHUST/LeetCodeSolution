class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
        vector<int> res;
        vector<int>::iterator it;
        vector<int>::iterator i;
        for(it = findNums.begin();it!=findNums.end();it++)
        {
            i=find(nums.begin(),nums.end(),*it);
            if(i==nums.end())
                res.push_back(-1);
            else
            {
                i++;
                for(;i!=nums.end();i++)
                {
                   if(*i>*it)
                   {
                       res.push_back(*i);
                       break;
                   }
                }
                if(i==nums.end())
                    res.push_back(-1);   
            }  
        }
        return res;
    }
};
