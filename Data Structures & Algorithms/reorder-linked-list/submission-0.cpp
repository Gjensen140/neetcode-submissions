/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        // Empty List
        if (!head) {
            return;
        }

        // Finding the middle node
        struct ListNode* slow = head;
        struct ListNode* fast = head;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Reversing second half of our linkedList
        struct ListNode* cur = slow->next;
        struct ListNode* prev = NULL;
        slow->next = NULL;

        while (cur) {
            struct ListNode* temp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = temp;
        }

        // Cur now stores the head of our reverse linkedlist
        struct ListNode* first = head;
        struct ListNode* second = prev;

        while (second) { // `second` half is always equal or shorter in length
            ListNode* tmp1 = first->next;
            ListNode* tmp2 = second->next;

            first->next = second;
            second->next = tmp1;

            first = tmp1;
            second = tmp2;
        }

        

    }
};
