# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp_head = head
        val_list = []
        while(True):
            temp_k = 0
            temp_val_list = []
            while(temp_k < k and head):
                temp_val_list.append(head.val)
                temp_k += 1
                head = head.next
            if(temp_k == k):
                val_list.extend(temp_val_list[::-1])
            else:
                break

        head = temp_head
        for val in val_list:
            head.val = val
            head = head.next

        return temp_head
        