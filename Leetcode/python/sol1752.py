#
#
# class Solution:
#     def check(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             prev = i
#             isGood = True
#             for _ in range(len(nums)-1):
#                 if nums[prev] > nums[(prev+1)%len(nums)]:
#                     isGood = False
#                     break
#                 prev = (prev+1)%len(nums)
#             if isGood:
#                 return True
#         return False


x = 12
print(x&1)
x<<=1
print(x)
x<<=1
print(x)
