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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // Nodes to store our output
        struct ListNode *cur = NULL;
        struct ListNode *head;
        int carry = 0;
        
        // Iterating through l1 and l2
        while (l1 && l2) {

            struct ListNode *temp = (struct ListNode *)malloc(sizeof(struct ListNode));
            temp->next = NULL;

            // Assigning the value to our output list
            int sum = l1->val + l2->val + carry;
            temp->val = (sum % 10);
            carry = sum / 10;

            l1 = l1->next;
            l2 = l2->next;

            // First node
            if (!cur) {
                cur = temp;
                head = cur;
            } 
            else {
                cur->next = temp;
                cur = cur->next;
            }

        }

        // Handling uneven lists
        while (l1) {
            struct ListNode *temp = (struct ListNode *)malloc(sizeof(struct ListNode));
            temp->next = NULL;
            
            int sum = carry + l1->val;
            temp->val = sum % 10;
            carry = sum / 10;
            
            l1 = l1->next;
            cur->next = temp;
            cur = cur->next;
        }
        while (l2) {
            struct ListNode *temp = (struct ListNode *)malloc(sizeof(struct ListNode));
            temp->next = NULL;

            int sum = carry + l2->val;
            temp->val = sum % 10;
            carry = sum / 10;

            l2 = l2->next;
            cur->next = temp;
            cur = cur->next;
        }

        if (carry) {
            struct ListNode *temp = (struct ListNode *)malloc(sizeof(struct ListNode));
            temp->next = NULL;
            temp->val = carry;
            cur->next = temp;
        }

        return head;
    }
};
