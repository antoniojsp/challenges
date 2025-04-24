# https://leetcode.com/problems/maximum-69-number/description/
class Solution:
    def separate(self, num :int) -> list[int]:
        """
        Split the number
        """
        rslt = []
        while 1 <= num:
            rslt.append(num%10)
            num//=10
        return rslt[::-1]

    def transform_list_to_int(self, nums :list) -> int:
        i = len(nums) - 1
        rslt: int = 0
        for j in nums:
            rslt+=( j*10**i)
            i-=1
        return rslt

    def maximum69Number (self, num:int) -> int:
        num_list = self.separate(num)
        for i, j in enumerate(num_list):
            if j == 6:
                num_list[i] = 9
                break

        return self.transform_list_to_int(num_list)
