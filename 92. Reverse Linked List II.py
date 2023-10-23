# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if(left == right):
            return head

        temp_head = head
        current_index = 1
        val_list = []
        while(current_index < left):
            head = head.next
            current_index += 1

        while(current_index <= right):
            val_list.append(head.val)
            head = head.next
            current_index += 1

        head  = temp_head
        current_index = 1
        while(current_index < left):
            head = head.next
            current_index += 1

        for val in val_list[::-1]:
            head.val = val
            head = head.next

        return temp_head