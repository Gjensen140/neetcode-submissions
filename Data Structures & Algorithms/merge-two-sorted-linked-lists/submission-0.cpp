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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        // Handling empty lists
        if (!list1) {
            return list2;
        }
        else if (!list2) {
            return list1;
        }

        // Storing the head of our list
        struct ListNode* head = NULL;
        if (list1->val <= list2->val) {
            head = list1;
            list1 = list1->next;
        }
        else {
            head = list2;
            list2 = list2->next;
        }

        // Pointer to track where we are in the list
        struct ListNode* cur = head;

        while (list1 && list2) {
            // List one value is smaller or equal
            if (list1->val <= list2-> val) {
                cur->next = list1;
                list1 = list1->next;
            } // List two value is smaller
            else {
                cur->next = list2;
                list2 = list2->next;
            }

            cur = cur->next;
        }

        // Adding the rest of the list that isn't null
        while (list1) {
            cur->next = list1;
            cur = cur->next;
            list1 = list1->next;
        }
        while (list2) {
            cur->next = list2;
            cur = cur->next;
            list2 = list2->next;
        }

        return head;
    }
};
