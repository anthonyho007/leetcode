/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    
    public TreeNode helper(TreeNode root, int v1, int v2) {
        
        if (root.val >= v1 && root.val <= v2) {
            return root;
        }
        TreeNode node = null;
        if (root.val > v2 && root.left != null) {
            node = helper(root.left, v1, v2);
        } else if (root.val < v1 && root.right != null) {
            node = helper(root.right, v1, v2);
        }
        return node;
        
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        int v1 = Math.min(p.val, q.val);
        int v2 = Math.max(p.val, q.val);
        return helper(root, v1, v2);
        
    }
}
