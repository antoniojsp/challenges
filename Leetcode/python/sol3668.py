# https://leetcode.com/problems/restore-finishing-order/
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends = set(friends) # fast lookpup friends
        return [i for i in order if i in friends] # check order and add to result if found in friends set
