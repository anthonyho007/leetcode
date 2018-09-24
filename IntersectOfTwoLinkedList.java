/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public Integer getListSize(ListNode head) {
        int size = 0;
        while (head != null) {
            size++;
            head = head.next;
        }
        return size;
    }
    
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        
        ListNode intersect = null;
        
        int sizeA = getListSize(headA);
        int sizeB = getListSize(headB);
        int min = Math.min(sizeA, sizeB);
        
        while (sizeA != min) {
            headA = headA.next;
            sizeA--;
        }
        
        while (sizeB != min) {
            headB = headB.next;
            sizeB--;
        }
        
        int ctr = 0;
        while (ctr < min) {
            if (headA.val == headB.val) {
                intersect = headA;
                break;
            }
            ctr++;
            headA = headA.next;
            headB = headB.next;
        }
        
        return intersect;
    }
}
