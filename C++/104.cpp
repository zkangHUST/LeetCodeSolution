/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        int a,b;
        if(root==NULL)
            return 0;
        else
        {
            a=1+maxDepth(root->left);
            b=1+maxDepth(root->right);
            return a>b?a:b;
            
        }
    }
};
