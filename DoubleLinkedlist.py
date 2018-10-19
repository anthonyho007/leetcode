class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        ctr = 0
        curr = self.head
        while ctr != index:
            curr = curr.next
            ctr += 1
        
        return curr.val
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:            
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.size += 1
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < 0 or index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            #middle
            node = Node(val)
            prev = None
            curr = self.head
            ctr = 0
            while ctr != index:
                prev = curr
                curr = curr.next
                ctr += 1
            prev.next = node
            node.prev = prev
            curr.prev = node
            node.next = curr
            self.size += 1
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or index >= self.size:
            return
        
        if self.size == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            self.head = head.next
        elif index == self.size - 1:
            self.tail = self.tail.prev
        else:
            curr = self.head
            prev = None
            ctr = 0
            while ctr != index:
                prev = curr
                curr = curr.next
                ctr += 1
            prev.next = curr.next
            curr.next.prev = prev
        self.size -= 1
        
            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
