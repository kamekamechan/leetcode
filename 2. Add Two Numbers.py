# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        for_calc_output = output
        add_up = 0
        while(True):
            if(l1 is not None and l2 is not None):
                for_calc_output.val = (l1.val + l2.val + add_up) % 10
                add_up = (l1.val + l2.val + add_up) // 10
                l1, l2 = l1.next, l2.next
            elif(l1 is None and l2 is not None):
                for_calc_output.val = (l2.val + add_up) % 10
                add_up = (l2.val + add_up) // 10
                l2 = l2.next
            elif(l1 is not None and l2 is None):
                for_calc_output.val = (l1.val + add_up) % 10
                add_up = (l1.val + add_up) // 10
                l1 = l1.next

            if(l1 is None and l2 is None):
                if(add_up != 0):
                    for_calc_output.next = ListNode(add_up)
                break
            else:
                for_calc_output.next = ListNode()
                for_calc_output = for_calc_output.next
        return output