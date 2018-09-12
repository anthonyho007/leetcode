# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class NodeW:
    def __init__(self, node, level):
        self.node = node
        self.level = level

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        queue = []
        rootNode = NodeW(root, 0)
        queue.append(rootNode)
        result = []
        temp = []
        currLevel = 0
        while len(queue) != 0:
            nodew = queue.pop(0)
            if nodew.level != currLevel:
                result.append(temp[:])
                temp.clear()
                currLevel += 1
            temp.append(nodew.node.val)
            if nodew.node.left != None:
                queue.append(NodeW(nodew.node.left, nodew.level + 1))
            if nodew.node.right != None:
                queue.append(NodeW(nodew.node.right, nodew.level + 1))
                
        if len(temp) != 0:
            result.append(temp[:])
        return result
