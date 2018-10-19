"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if head == None:
            return Node(insertVal, None)
        
        prev = head
        curr = head.next
        if curr != None:            
            while True:
                if prev.val <= insertVal and curr.val >= insertVal:
                    break
                elif prev.val > curr.val and (prev.val <= insertVal or curr.val >= insertVal):
                    break
                if head == curr:
                    break
                prev = curr
                curr = curr.next

        node = Node(insertVal, curr)
        prev.next = node
        return head
