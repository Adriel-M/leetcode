# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        smallest_num = -sys.maxsize - 1
        biggest_num = sys.maxsize

        def isValid(curr_node, min_num, max_num):
            if curr_node.val <= min_num or curr_node.val >= max_num:
                return False
            if curr_node.left is not None and not isValid(curr_node.left, min_num, curr_node.val):
                return False
            if curr_node.right is not None and not isValid(curr_node.right, curr_node.val, max_num):
                return False
            return True
        if not root:
            return True
        else:
            return isValid(root, smallest_num, biggest_num)
