class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def test(self, head: Optional[ListNode]) -> bool:
        slow_node = head
        fast_node = head
        while(fast_node != None and fast_node.next != None):
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if(slow_node == fast_node):
                return True
        return False
