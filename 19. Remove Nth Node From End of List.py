# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_list = 0
        temp_head = head

        while(head):
            len_list += 1
            head = head.next
        head = temp_head
        if(len_list >= 3):
            if(n == len_list):
                return head.next
            jump = len_list - n - 1
            while(jump > 0):
                jump -= 1
                head = head.next
            head.next = head.next.next
            return temp_head
        elif(len_list == 2):
            if(n == 1):
                return ListNode(head.val)
            return head.next
        return None