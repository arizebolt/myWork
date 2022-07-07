# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    s = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return root
        self.bstToGst(root.right)
        root.val = root.val + self.s
        self.s = root.val
        self.bstToGst(root.left)
        return root