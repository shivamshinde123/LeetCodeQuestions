# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        ## Approach 1: quite slow
        # encountered_by_A = set()

        # current_head_a = headA
        # current_head_b = headB

        # while current_head_a:
        #     encountered_by_A.add(current_head_a)
        #     current_head_a = current_head_a.next

        # while current_head_b:
        #     if current_head_b in encountered_by_A:
        #         return current_head_b
            
        #     current_head_b = current_head_b.next

        # Approach 2: 
        """
         For this approach, we will initialize two pointers which is pointing to heads of each Linked List. Then we will make these pointers run through both the Linked Lists ie. n + m length. By doing so, we will hit an intersection point.
        """

        one = headA
        two = headB

        while one != two:
            if one is None:
                one = headB
            else:
                one = one.next

            if two is None:
                two = headA
            else:
                two = two.next

        return one






        
        