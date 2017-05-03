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
    TreeNode* invertTree(TreeNode* root) {
        if(root==NULL)
        {
            return root;
        }
        else if(root->left!=NULL||root->right!=NULL)
        {
            invertTree(root->left);       //转置左子树
            invertTree(root->right);      //转置右子树
            TreeNode* p = root->left;     //交换左右子树指针
            root->left=root->right;
            root->right=p;
        }
        return root;
        
    }
};
