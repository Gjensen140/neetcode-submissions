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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        struct ListNode* cur = head;
        int length = 0;

        while (cur) {
            length += 1;
            cur = cur->next;
        }


        struct ListNode* prev = head;
        cur = head;

        for (int i = 0; i < (length - n); i++) {
            prev = cur;
            cur = cur->next;
        }

        if (cur != prev) {
            prev->next = cur->next;
            cur->next = NULL;
            return head;
        }
        else {
            cur = cur->next;
            prev->next = NULL;
            return cur;
        }
    }
};
