# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        # edge case
        if l1 == None and l2 == None:
            return head
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        #set head
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        curr = head
        
        # splice lists
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
        # append remaining
        if l1 != None:
            curr.next = l1
        if l2 != None:
            curr.next = l2
        return head
