"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_head_pointer_list = {}

        temp_head = head

        if(head is None):
            return None
            
        copy_head = Node(head.val)
        copy_head_pointer_list[head] = copy_head
        copy_head = copy_head.next
        head = head.next

        while(head):
            copy_head_pointer_list[head] = Node(head.val)
            head = head.next
        
        head = temp_head
        while(head):
            copy_head_pointer_list[head].next = copy_head_pointer_list.get(head.next)
            copy_head_pointer_list[head].random = copy_head_pointer_list.get(head.random)
            head = head.next

        return copy_head_pointer_list[temp_head]

        

        