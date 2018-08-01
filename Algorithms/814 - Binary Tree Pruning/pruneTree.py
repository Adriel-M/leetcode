class Solution:
    def prune(self, root):
        should_delete = True
        if root.val == 1:
            should_delete = False
        if root.left:
            should_delete_left = self.prune(root.left)
            if should_delete_left:
                root.left = None
            else:
                should_delete = False
        if root.right:
            should_delete_right = self.prune(root.right)
            if should_delete_right:
                root.right = None
            else:
                should_delete = False
        return should_delete

    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.prune(root)
        return root
