class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    s = 0 
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root is None:
            return
        #s = 0
        def helper(root):
            if root is None:
                return 
            if root.val % 2 ==0:
                if root.left:
                    if root.left.left:
                        self.s = self.s + root.left.left.val
                    if root.left.right:
                        self.s = self.s + root.left.right.val
                if root.right:
                    if root.right.left:
                        self.s = self.s + root.right.left.val    
                    if root.right.right:
                        self.s = self.s + root.right.right.val
                
            helper(root.left)
            helper(root.right)
            
            return self.s 
        ans = helper(root)
        return ans