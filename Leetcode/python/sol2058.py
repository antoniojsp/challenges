
# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def min_dist(self, arr:list)->int:
        '''
        find the minimum distance between critical points
        '''
        lowest = float('inf')
        for i in range(len(arr)-1):
            lowest = min(lowest, abs(arr[i+1] - arr[i]))
        return lowest

    def max_dist(self, arr:list)->int:
        '''
        find the maximum distance between critical points
        '''
        return arr[-1] - arr[0] # arr is in order so min and max are located on the extreemes

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ans = [] # store the critical points
        curr = head.next # starts scanning from node 1 in a 0-index system
        prev = head
        i = 1
        while curr.next:
            if prev.val < curr.val > curr.next.val \
                or prev.val > curr.val < curr.next.val: # add critical points to and
                ans.append(i)
            i += 1
            prev = curr
            curr = curr.next

        if len(ans) < 2: # if less than 2 critical points, then no distances can be found
            return [-1,-1]

        mini = self.min_dist(ans)
        maxi = self.max_dist(ans)
        return [mini, maxi]