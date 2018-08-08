/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrderBottom = function (root) {
  if (!root) {
    return [];
  }
  let currLevel = [root];
  let ret = [];
  while (currLevel.length > 0) {
    let retLevel = [];
    let nextLevel = [];
    for (let i = 0; i < currLevel.length; i++) {
      retLevel.push(currLevel[i].val);
      if (currLevel[i].left) {
        nextLevel.push(currLevel[i].left);
      }
      if (currLevel[i].right) {
        nextLevel.push(currLevel[i].right);
      }
    }
    currLevel = nextLevel;
    ret.push(retLevel);
  }
  return ret.reverse();
};
