class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(not (list1 and list2)):
            return list1 or list2
        
        if(list1.val<=list2.val):
            a1, a2 = list1, list2
        else:
            a1, a2 = list2, list1

        output = a1
        temp = a1
        a1 = a1.next
        
        while(a1 and a2):
            try:
                if(a1.val <= a2.val):
                    temp.next = a1
                    a1 = a1.next
                else:
                    temp.next = a2
                    a2 = a2.next
            except AttributeError:
                pass
            
            temp = temp.next

        if(a1):
            temp.next = a1
        else:
            temp.next = a2

        return output