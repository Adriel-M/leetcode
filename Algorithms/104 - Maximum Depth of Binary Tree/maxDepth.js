/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function (root) {
  let ret = 0;
  const traverse = (currNode, currDepth) => {
    if (!currNode.left && !currNode.right) {
      ret = Math.max(ret, currDepth);
    } else {
      if (currNode.left) {
        traverse(currNode.left, currDepth + 1);
      }
      if (currNode.right) {
        traverse(currNode.right, currDepth + 1);
      }
    }
  }
  if (root) {
    traverse(root, 1);
  }
  return ret;
};