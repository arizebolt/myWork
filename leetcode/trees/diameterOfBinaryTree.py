# Definition for a binary tree node.
from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    d = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #len = 0
        
        def helper(root):
            if root is None:
                return 0
            
            else:
                lmax = helper(root.left) 
                rmax = helper(root.right) 
                self.d = max(self.d,lmax+rmax) 
                
                return max(lmax,rmax) + 1
        helper(root)
        return self.d
            
        