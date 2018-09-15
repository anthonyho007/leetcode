# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwoLists(l1, l2):
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
        if len(lists) == 0:
            return None
        lst = lists[:]
        while len(lst) != 1:
            tmp = []
            n = len(lst)
            i1, i2 =  0, 1
            while i1 < n and i2 < n:
                res = mergeTwoLists(lst[i1], lst[i2])
                tmp.append(res)
                i1 += 2
                i2 += 2
            if i1 == n-1:
                tmp.append(lst[n-1])
            lst = tmp[:]
        return lst[0]
