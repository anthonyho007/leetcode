/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) {
            return null;
        }
        
        RandomListNode curr = head;
        
        while (curr != null) {
            RandomListNode copy = new RandomListNode(curr.label);
            copy.next = curr.next;
            curr.next = copy;
            curr = copy.next;
        }
        curr = head;
        while (curr != null) {
            if (curr.random != null) {
                RandomListNode copy = curr.next;
                copy.random = curr.random.next;
            }
            curr = curr.next.next;
        }
        
        
        RandomListNode copyHead = head.next;
        curr = head;
        while (curr != null) {
            RandomListNode temp = curr.next;
            curr.next = temp.next;
            if (temp.next != null) {
                temp.next = temp.next.next;
            }
            curr = curr.next;
        }
        
        return copyHead;
    }
}
