/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* prev=NULL,*temp=head,*nextnode=head;
    while(nextnode!=NULL){
        nextnode=temp->next;
        temp->next=prev;
        prev=temp;
        temp=nextnode;
    }
    return prev;
    
}