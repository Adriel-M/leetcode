# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None and q is not None:
            return False
        elif p is not None and q is None:
            return False
        elif p.val != q.val:
            return False
        else:
            if not self.isSameTree(p.left, q.left):
                return False
            elif not self.isSameTree(p.right, q.right):
                return False
            else:
                return True
