# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.count = 0
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if root.left == None and root.right == None:
                self.count += 1
                return True
            res1 = False
            res2 = False
            if root.left == None:
                res1 = helper(root.right)
                if res1 == True and root.val == root.right.val:
                    self.count += 1
                    return True
                return False
            elif root.right == None:
                res2 = helper(root.left)
                if res1 == True and root.val == root.left.val:
                    self.count += 1
                    return True
                return False
            else:
                res1 = helper(root.right)
                res2 = helper(root.left)
                if root.val == root.left.val and root.val == root.right.val:
                    self.count += 1
                    return True
                return False
        if root == None:
            return 0
        helper(root)
        return self.count
