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
    bool hasCycle(ListNode* head) {
        if (!head) {
            return false;
        }

        // Nodes to iterate through the list at different speeds
        struct ListNode* fast = head->next;
        struct ListNode* slow = head;

        // Iterating through
        while (fast) {
            // If they're the same, there's a cycle
            if (fast == slow) {
                return true;
            }

            // Progressing
            slow = slow->next;

            // If the next node exists
            if (fast->next){
                fast = fast->next->next;
            }
            else {
                return false;
            }
            
        }

        return false;
    }
};
