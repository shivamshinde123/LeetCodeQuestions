/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
let getIntersectionNode = function(headA, headB) {
    let one = headA
    let two = headB

    while (one !== two){
        if (one === null){
            one = headB
        }
        else{
            one = one.next
        }

        if (two === null){
            two = headA
        }
        else{
            two = two.next
        }
    }

    return one
};