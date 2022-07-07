# Definition for a binary tree node.
from ast import List

from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if nums:
            maxNum = max(nums)
            index = nums.index(maxNum)
            root = TreeNode(maxNum)
            root.left = self.constructMaximumBinaryTree(nums[:index])
            root.right = self.constructMaximumBinaryTree(nums[index+1:])
            nums.pop(index)
            return root
            
        