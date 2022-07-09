# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from ast import List

from pyparsing import Optional
from leetcode.trees.averageOfSubtree import TreeNode


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return 
        q = [] 
        def helper(root,q):
            if root is None:
                return 
            else :
                helper(root.left,q)
                q.append(root.val)
                helper(root.right,q)
        helper(root,q)
        #q.sort()
        counts = {}
    # iterate through the list
        for item in q:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1
        # get the keys with the max counts
        return [key for key in counts.keys() if counts[key] == max(counts.values())]
            
                
        