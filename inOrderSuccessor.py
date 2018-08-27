class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        def helper(root, p):
            if p.right != None:
                succesor = p.right
                while succesor.left != None:
                    succesor = succesor.left
                
                return succesor
            succesor = None
            curr = root
            while curr != None:
                if curr.val == p.val:
                    break
                if curr.val < p.val:
                    curr = curr.right
                else:
                    succesor = curr
                    curr = curr.left
            return succesor
        return helper(root,p)
