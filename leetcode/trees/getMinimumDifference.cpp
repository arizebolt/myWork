/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int pre=-1;
    int ans=INT_MAX;
    int getMinimumDifference(TreeNode* root) {
        if(root==NULL)
            return ans;
        getMinimumDifference(root->left);
        if(pre!=-1)
            ans=min(ans,(root->val-pre));
        pre=root->val;
        getMinimumDifference(root->right);
        return ans;
    }
};