
//https://leetcode.com/problems/reverse-linked-list/

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function reverseList(head: ListNode | null): ListNode | null {
    if(!head || !head.next){
        return head
    }

    let newHead = reverseList(head.next)
    head.next.next = head
    head.next = null

    return newHead



    // if (!head){
    //     return head;
    // }
    // let prev = null;
    // let node:ListNode = head;

    // while(node){
    //     let next = node.next;
    //     node.next = prev;
    //     prev = node
    //     node = next;
    // }

    // return prev;
};