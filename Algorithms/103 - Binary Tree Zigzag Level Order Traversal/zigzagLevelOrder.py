# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret = []
        curr_level = [root]
        curr_rank = 0
        while len(curr_level) > 0:
            if curr_rank % 2 == 0:
                ret.append([node.val for node in curr_level])
            else:
                ret.append([node.val for node in reversed(curr_level)])
            new_level = []
            for node in curr_level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            curr_rank += 1
            curr_level = new_level
        return ret
