class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        v = l1.val + l2.val
        carry = v / 10
        head = ListNode(v % 10)
        curr = head
        l1, l2 = l1.next, l2.next
        
        while l1 != None or l2 != None:
            if l1 != None and l2 != None:
                v = l1.val + l2.val + carry
                carry = v / 10
                l1, l2 = l1.next, l2.next
            elif l1 != None:
                v = l1.val + carry
                carry = v /10
                l1 = l1.next
            else:
                v = l2.val + carry
                carry = v /10
                l2 = l2.next

            temp = ListNode(v % 10)
            curr.next = temp
            curr = temp
        if carry != 0:
            curr.next = ListNode(carry)
        return head
