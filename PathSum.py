# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        def helper(node, val):
            if node == None:
                return False
            if node.left == None and node.right == None:
                if node.val + val == sum:
                    return True
            return helper(node.left,val + node.val) or helper(node.right, val + node.val)
        return helper(root, 0)
