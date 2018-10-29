# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        def helper(inorder, postorder, li,ri, lp, rp):
            if li > ri or lp > rp:
                print("end")
                return None
            if rp < 0 or rp >= len(inorder):
                return None
            root = TreeNode(postorder[rp])
            ctr = 0
            while inorder[ctr+ li] != root.val:
                ctr += 1
            lnode = helper(inorder, postorder, li, ctr + li-1, lp, lp + ctr-1)
            rnode = helper(inorder,postorder, li+ctr+1, ri, lp + ctr, rp-1)
            root.left = lnode
            root.right = rnode
            return root
        n = len(inorder)
        return helper(inorder, postorder, 0, n-1, 0, n-1)
