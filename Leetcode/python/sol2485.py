# #  https://leetcode.com/problems/find-the-pivot-integer/description/
# class Solution:
#     def pivotInteger(self, n: int) -> int:
#
#         left = [1]
#         for i in range(2 , n +1):
#             left.append(left[-1 ] +i)
#
#         right = [n]
#         for i in range( n -1, 0, -1):
#             right.append(right[-1 ] +i)
#         right.reverse()
#         i = 0
#         while i < len(left):
#             if left[i] == right[i]:
#                 return i+ 1
#             i += 1
#         return -1
#
from collections import  Counter
c = Counter(a=4, b=2, c=0, d=-2)
print(sorted(c.elements()))
