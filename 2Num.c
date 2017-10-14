/**
 * Definition for singly-linked list.
 * struct ListNode {}
 *     int val;
 *     struct ListNode *next;
 * };
 */

#include <stdlib.h>

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int carry = 0; 
    int digit;
    int d1, d2;
    struct ListNode  *head;
    struct ListNode  *current;
    struct ListNode  *new_node;
    head = (struct ListNode*)malloc(sizeof(struct ListNode));
    current = head;
    struct ListNode  *prev;
    while ( l1 != NULL || l2 != NULL){
        if (l1 == NULL)
            d1 = 0;
        else
            d1 = l1->val;
        if (l2 == NULL)
            d2 = 0;
        else
            d2 = l2->val;
        digit = (d1 + d2 + carry) % 10;
        carry = (d1 + d2 + carry) / 10;
        new_node = (struct ListNode *)malloc(sizeof(struct ListNode));
        current->val = digit;
        current->next = new_node;
        prev = current;
        current = new_node;
        if (l1 != NULL)
            l1= l1->next;
        if (l2 != NULL)
            l2= l2->next;
    }
    if ( carry > 0){
        current->val = carry;
        current->next = NULL;
    } else {
        free(current);
        prev->next = NULL;
    }
    return head;
}