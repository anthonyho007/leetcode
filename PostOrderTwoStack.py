"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        stack = []
        result = []
        if root == None:
            return result
        
        stack.append(root)
        
        while len(stack) != 0:
            node = stack.pop()
            result.insert(0,node.val)
            for child in node.children:
                stack.append(child)
        
        return result
