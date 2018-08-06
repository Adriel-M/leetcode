# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []

        def traverse(curr_node):
            if curr_node:
                if curr_node.left is not None:
                    traverse(curr_node.left)
                ret.append(curr_node.val)
                if curr_node.right is not None:
                    traverse(curr_node.right)
        traverse(root)
        return ret
