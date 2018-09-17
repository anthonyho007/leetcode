/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    
    public TreeLinkNode helper(TreeLinkNode node) {
        TreeLinkNode prev = null;
        TreeLinkNode firstChild = null;
        TreeLinkNode nextChild = null;
        
        if (node == null) {
            return node;
        }
        
        while (node != null) {
            
            while (node != null && node.left == null && node.right == null) {
                node = node.next;
            }
            
            if (node != null && node.left != null && node.right  != null) {
                node.left.next = node.right;
                nextChild = node.right;
                if (prev == null) {
                    firstChild = node.left;
                } else {
                    prev.next = node.left;
                }
            } else {
                nextChild = (node == null) ? null : (node.left == null) ? node.right : node.left;
                if (prev == null) {
                    firstChild = nextChild;
                } else {
                    prev.next = nextChild;
                }
            }
            node = (node == null) ? null : node.next;
            prev = nextChild;
        }
        
        return firstChild;
        
    }
    
    public void connect(TreeLinkNode root) {
        TreeLinkNode head = root;
        TreeLinkNode nextHead = null;
        nextHead = helper(root);
        while (nextHead != null) {
            nextHead = helper(nextHead);
        }
    }
}
