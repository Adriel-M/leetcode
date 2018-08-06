# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ret = []
        curr_stack = []

        def generate(curr_node, curr_sum):
            calc_val = curr_node.val + curr_sum
            curr_stack.append(curr_node.val)
            if calc_val == target and curr_node.left is None and curr_node.right is None:
                ret.append(curr_stack[:])
            if curr_node.left is not None:
                generate(curr_node.left, calc_val)
            if curr_node.right is not None:
                generate(curr_node.right, calc_val)
            curr_stack.pop()
        if root:
            generate(root, 0)
        return ret
