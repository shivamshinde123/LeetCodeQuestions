# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # The length of the linked list is needed
#         def get_node(index):
#             current = head
#             for _ in range(index):
#                 current = current.next
#             return current
        
#         def get_length():
#             current = head
#             length = 0
#             while current:
#                 length += 1
#                 current = current.next
#             return length
                
#         length = get_length()
#         if length % 2 == 1:
#             return get_node(((length + 1) // 2) - 1)
#         else:
#             return get_node(length // 2)
        
        # Without calculating the length of the linked list (tortoise and hare algorithm or slow and fast pointer approach)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow