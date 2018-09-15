# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class NodeW:
    def __init__(self, node, level):
        self.node = node
        self.level = level

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        queue = []
        queue.append(NodeW(root,0))
        
        while len(queue) != 0:
            node = queue.pop(0)
            if len(queue) != 0 and queue[0].level == node.level:
                node.node.next = queue[0].node
            else:
                node.node.next = None
            if node.node.left:
                queue.append(NodeW(node.node.left, node.level + 1))
            if node.node.right:
                queue.append(NodeW(node.node.right, node.level + 1))
