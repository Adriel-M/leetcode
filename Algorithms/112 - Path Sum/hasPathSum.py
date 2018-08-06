class Solution:
    def hasPathSum(self, root, target):
        def check(curr_node, curr_val):
            calc_val = curr_val + curr_node.val
            if calc_val == target and curr_node.left is None and curr_node.right is None:
                return True
            elif curr_node.left is not None and check(curr_node.left, calc_val):
                return True
            elif curr_node.right is not None and check(curr_node.right, calc_val):
                return True
            else:
                return False
        if not root:
            return False
        return check(root, 0)
