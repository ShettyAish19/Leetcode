# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        local=[]
        if not head or head.next is None or head.next.next is None:
            return [-1,-1]
        prev=head

        cur=head.next
        count=1
        while cur.next is not None:
            count+=1
            if cur.val>prev.val and cur.val>cur.next.val:
                local.append(count)

            elif cur.val<prev.val and cur.val<cur.next.val:
                local.append(count)

            prev=cur
            cur=cur.next
        if not local:
            return [-1,-1]
        print(local)
        mini=float('inf')
        for i in range(len(local)-1):
            if local[i+1]-local[i]<mini:
                mini=local[i+1]-local[i]
        maxi=-1
        if len(local)>=2:
            maxi=local[len(local)-1]-local[0]

        if mini !=float('inf'):
            return [mini,maxi]

        else:
            return [-1,-1]


        