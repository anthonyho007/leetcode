
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    private boolean isFirstNodeFound = false;
    private boolean isDone = false;
    private TreeNode lca = null;
    public boolean helper(TreeNode node, TreeNode p, TreeNode q) {
        if (node == null) {
            return false;
        }
        
        if (isDone) return false;
        boolean left = helper(node.left, p, q);
        if (isDone) return false;
        boolean right = helper(node.right, p, q);
        
        boolean mid = false;
        if (node.val == p.val || node.val == q.val) {
            mid = true;
        }
        
        if (left && right || mid && left || mid && right) {
            lca = node;
            isDone = true;
            return false;
        }
        
        return left || right || mid;
        
        
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        helper(root, p,q);
        return lca;
    }
}
