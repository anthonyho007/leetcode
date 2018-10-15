# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return head
        
        odd = head
        even = head.next
        mid = even
        
        if head.next != None:
            curr = head.next.next
            ctr = 1
            while curr != None:
                if ctr % 2 == 1:
                    odd.next = curr
                    odd = odd.next
                else:
                    even.next = curr
                    even = even.next
                curr = curr.next
                ctr += 1
        odd.next = mid
        if even != None:
            even.next = None
        return head
        
