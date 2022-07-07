# Definition for a binary tree node.
from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = []
        if root is None:
            return 
        q.append(root)
        
        while len(q) > 0:
            total = 0
            for i in range(len(q)):
                ele = q.pop(0)
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
                total = total + ele.val
        return total
                