# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        # Create pointers
        pointer_1 = list1 
        pointer_2 = list2

        # Create new list with dummy head and tail
        dummy = ListNode()
        tail = dummy

        while pointer_1 and pointer_2:
            if pointer_1.val <= pointer_2.val:
                tail.next = pointer_1
                pointer_1 = pointer_1.next
            else:
                tail.next = pointer_2
                pointer_2 = pointer_2.next
            
            tail = tail.next
        
        # Check if any nodes are remaining and attatch them on the tail
        if pointer_1:
            tail.next = pointer_1
        else:
            tail.next = pointer_2


        return dummy.next
                
