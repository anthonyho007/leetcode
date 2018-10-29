# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        def helper(r1, r2):
            if r1 == None and r2 == None:
                return True
            
            if r1 != None and r2 != None and r1.val == r2.val:
                res1 = helper(r1.left, r2.right)
                res2 = helper(r1.right, r2.left)
                return res1 and res2
            return False
        return helper(root.left, root.right)
