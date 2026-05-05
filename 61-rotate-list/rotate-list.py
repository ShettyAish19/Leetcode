# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head

        n=1
        temp=head
        while temp.next!=None:
            temp=temp.next
            n+=1

        k=k%n
        if k==0:
            return head

        temp.next=head
        new_temp=head
        steps=n-k-1
        for _ in range(steps):
            new_temp=new_temp.next

        head=new_temp.next
        new_temp.next=None

        return head


        


        