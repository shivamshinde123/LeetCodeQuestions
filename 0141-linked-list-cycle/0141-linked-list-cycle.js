/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    let encountered_nodes = new Set([]);
    let current_node = head

    while (current_node) {
        if (encountered_nodes.has(current_node)){
            return true
        }
        encountered_nodes.add(current_node)
        current_node = current_node.next
    }

    return false

};