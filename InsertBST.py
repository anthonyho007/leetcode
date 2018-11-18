# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def insert(root, val):
            if root == None:
                return TreeNode(val)
            if root.val < val:
                root.right = insert(root.right, val)
            else:
                root.left = insert(root.left, val)
            return root
        
        return insert(root, val)
        
