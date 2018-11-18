# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.head = root
        self.curr = root

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.curr != None
        

    def next(self):
        """
        :rtype: int
        """
        tmp = None
        result = None
        
        while self.curr != None:
            if self.curr.left == None:
                result = self.curr.val
                self.curr = self.curr.right
                break
            else:
                tmp = self.curr.left
                while tmp.right != None and tmp.right != self.curr:
                    tmp = tmp.right
                if tmp.right == None:
                    tmp.right = self.curr
                    self.curr = self.curr.left
                else:
                    result = self.curr.val
                    tmp.right = None
                    self.curr = self.curr.right
                    break
        return result
                    
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
