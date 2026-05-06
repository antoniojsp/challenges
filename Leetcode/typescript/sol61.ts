
// https://leetcode.com/problems/rotate-list/submissions/1996771447/?envType=daily-question&envId=2026-05-05.


  class ListNode {
      val: number
      next: ListNode | null
      constructor(val?: number, next?: ListNode | null) {
          this.val = (val===undefined ? 0 : val)
          this.next = (next===undefined ? null : next)
      }
  }


const length = (node:any) => {
    let curr = node;
    let len = 0;
    while (curr){
        len++;
        curr = curr.next;
    }
    return len;
}

function rotateRight(head: ListNode | null, k: number): ListNode | null {
    const len = length(head)

    if(len <= 1 || k === 0){
        return head
    }
    const steps = k%len; // if steps is divisible by number of elements, then no movement is necessary
    if(steps === 0){ // if it's divisible ( k and len of list), then return head
        return head;

    }

    const new_start = len - steps - 1;
    console.log(new_start);
    let temp = head!;
    for(let i = 0; i < new_start; i++){
        temp = temp.next!;
    }
    let next_node =  temp.next!
    temp.next = null;
    let curr = next_node;
    while(curr.next){
        curr = curr.next
    }
    curr.next = head
    return next_node;
};