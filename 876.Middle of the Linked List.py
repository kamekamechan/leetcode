# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def singly_list_to_arr (self, list):
        arr = []
        data = list
        while(data != None):
            arr.append(data.val)
            data = data.next
        return arr

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = self.singly_list_to_arr(head)
        arr_half_len = math.floor(len(arr)/2)
        return_arr = arr[arr_half_len:]
        for i,x in enumerate(return_arr):
            if(i==0):
                return_list = ListNode(val=x,next=None)
            else:
                try:
                    temp_list.next = ListNode(val=x,next=None)
                    temp_list = temp_list.next
                except:
                    temp_list = ListNode(val=x,next=None) 
                    return_list.next = temp_list
        return return_list