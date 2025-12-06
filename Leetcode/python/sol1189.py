
# https://leetcode.com/problems/maximum-number-of-balloons/description/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        store = {i:0 for i in "balloon"}
        for i in text:
            if i in store:
                store[i]+=1
        mini =  min(store.values())
        if mini == 0: # if any char in "balloon" is zero, then no "balloon" can be form.
            return 0
        less = min(store["l"],store["o"])# look for the mini value between l and o
        return min(less//2, mini) # divide less by 2, if it's greater than the min freq of b, a or n, return mini



