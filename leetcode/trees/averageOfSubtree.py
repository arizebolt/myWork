# Definition for a binary tree node.
from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0,0,0
            left = dfs(root.left)
            right = dfs(root.right)
            if (left[0]+right[0]+root.val) // (left[1]+right[1]+1) == root.val:
                avg_true = 1
            else:
                avg_true = 0
            return (left[0]+right[0]+root.val, left[1]+right[1]+1, left[2]+right[2]+avg_true)
            
                
        return dfs(root)[2]
        #ans = dfs(root)
        #return ans[2]