# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.isPal = True
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        n = 0
        curr = head
        while curr != None:
            curr = curr.next
            n += 1
        isOld = True if n % 2 == 1 else False
        n /= 2
        
        def helper(node, ctr, mid,isOld):
            curr = node
            if ctr == mid +1 and isOld:
                return curr.next
            elif ctr == mid and not isOld:
                if self.isPal:
                    if node.val != node.next.val:
                        self.isPal = False
                return node.next.next
            else:
                target = helper(node.next, ctr+1, mid, isOld)
                if self.isPal:
                    if node.val != target.val:
                        self.isPal = False
                return target.next
        helper(head, 1, n, isOld)
        return self.isPal
        
