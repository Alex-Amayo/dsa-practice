# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #find middle       
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #reverse second half
        prev = None

        while slow:
            tmp = slow.next
            slow.next = prev
            

            prev = slow
            slow = tmp


        #merge the two sides
        first, second = head, prev

        while second.next:
            tmp_1, tmp_2 = first.next, second.next

            first.next = second
            second.next = tmp_1
            first = tmp_1
            second = tmp_2




