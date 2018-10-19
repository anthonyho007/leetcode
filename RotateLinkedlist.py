# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        size = 0
        curr = head
        end = curr
        while curr != None:
            size += 1
            end = curr
            curr = curr.next
        
        if k % size == 0:
            return head
        
        mv = size - 1 - (k % size)
        ctr = 0
        curr = head
        while ctr != mv:
            curr = curr.next
            ctr += 1
        end.next = head
        head = curr.next
        curr.next = None
        return head
        
        
        
        
