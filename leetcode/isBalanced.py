# Definition for a binary tree node.
from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root):
            if root is None:
                return 0
            lh = helper(root.left) 
            rh = helper(root.right) 
            if lh == -1 or rh == -1:
                return -1
            if abs(lh-rh) > 1:
                return -1
            return max(lh,rh) + 1
        if helper(root) == -1 :
            return False
        return True
    
        
        