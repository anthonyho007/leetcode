# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        stack = []
        stack.append(root)
        head = root
        result = []
        while len(stack) != 0:
            node = stack[-1]
            if (node.left == None and node.right == None) or (head == node.left or head == node.right): 
                head = stack.pop()
                result.append(head.val)
            else:
                if node.right != None:
                    stack.append(node.right)
                if node.left != None:
                    stack.append(node.left)
                
                
        return result
