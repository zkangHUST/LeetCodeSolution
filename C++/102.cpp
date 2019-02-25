/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 #include<queue>
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
    queue<TreeNode*> s;
    vector<vector<int>> ans;
    vector<int> temp;
    TreeNode* p;
    int count_up;//上一层节点个数
    int count_down = 0;//下一层节点个数
    if(root!=NULL)
    {
          s.push(root);
          count_up=1;
    }
    while(!s.empty())
    {
        p=s.front();
        s.pop();
        {
            temp.push_back(p->val);
            count_up--;
        }
        if(p->left!=NULL)
        {
            s.push(p->left);
            count_down++;
        }
        if(p->right!=NULL)
        {
            s.push(p->right);
            count_down++;
        }
        if(count_up==0)
        {
            ans.push_back(temp);
            temp.clear();
            count_up=count_down;
            count_down= 0;  
        }
    }
    return ans;
    }
};
