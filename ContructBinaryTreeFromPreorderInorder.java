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
    public void helper(int[] preorder, int[] inorder, TreeNode node) {
        if (preorder.length == 1) {
            return;
        }
        int i = 0;
        while(inorder[i] != preorder[0]) {
            i++;
        }
        int left_num = i;
        int right_num = inorder.length -1 -i;
        if (left_num != 0) {
            node.left = new TreeNode(preorder[1]);
            helper(Arrays.copyOfRange(preorder,1, left_num + 1), Arrays.copyOfRange(inorder,0, left_num), node.left);
        }

        // System.out.println(right_num);
        if (right_num != 0) {
            node.right = new TreeNode(preorder[left_num + 1]);
            helper(Arrays.copyOfRange(preorder,left_num + 1, preorder.length), Arrays.copyOfRange(inorder,left_num+1, inorder.length), node.right);

        }
    }
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length == 0) {
            return null;
        }
        TreeNode root = new TreeNode(preorder[0]);
        helper(preorder, inorder, root);
        return root;
    }
}
