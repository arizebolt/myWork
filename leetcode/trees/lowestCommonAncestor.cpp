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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        
        if(p->val < root->val && q->val < root->val)
		{
			return lowestCommonAncestor(root->left,p,q);
		}
		
		// Check if p and q values are greater than root value to shift to right of root node
		else if(p->val > root->val && q->val > root->val)
		{
			return lowestCommonAncestor(root->right,p,q);
		}
		
		return root;
    }
};