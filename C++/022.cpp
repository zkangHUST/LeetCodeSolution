class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string>res;
        DFS(res,n,n,"");
        return res;
        
    }
private:
    void DFS(vector<string>& res,int left,int right,string p)
    {
        if(left==0&&right==0)
        {
            res.push_back(p);
            return ;
        }
        if(left>0)
        {
            DFS(res,left-1,right,p+'(');
        }
        if(left<right)
        {
            DFS(res,left,right-1,p+')');
            
        }
        
    }
};
