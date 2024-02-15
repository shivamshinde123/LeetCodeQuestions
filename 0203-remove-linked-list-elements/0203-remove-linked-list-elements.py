# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode(0)
        sentinel.next = head
        current_node, previous_node = head, sentinel

        while current_node:
            if current_node.val == val:
                previous_node.next = current_node.next
            else:
                previous_node = current_node

            current_node = current_node.next

        return sentinel.next