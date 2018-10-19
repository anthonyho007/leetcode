"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def helper(node):
            if node.next == None and node.child == None:
                return node
            
            nxt = node.next
            child = None
            if node.child != None:
                node.child.prev = node
                node.next = node.child
                node.child = None
                child = helper(node.next)
            if child != None:
                child.next = nxt
                if nxt != None:
                    nxt.prev = child
            end = None
            if nxt != None:
                end = helper(nxt)
            
            return end
        if head == None:
            return head
        helper(head)
        return head
                
            
            
