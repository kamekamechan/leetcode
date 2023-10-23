# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp_head = head

        head = temp_head
        output_list = ListNode()
        for_output = output_list
        while(head):
            if(head.val < x):
                output_list.next = ListNode(head.val)
                output_list = output_list.next
            head = head.next

        head = temp_head
        while(head):
            if(head.val >= x):
                output_list.next = ListNode(head.val)
                output_list = output_list.next
            head = head.next

        return for_output.next
                
