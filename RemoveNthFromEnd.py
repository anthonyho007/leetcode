# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        end = head
        for i in range(n-1):
            end = end.next
        prev = None
        start = head
        while end != None:
            if end.next == None:
                break
            prev = start
            end = end.next
            start = start.next
            
        if prev == None:
            return start.next
        prev.next = start.next
        return head
