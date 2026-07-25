# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/?envType=daily-question&envId=2026-07-08
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        suma = [0]
        for i in s:
            suma.append(suma[-1 ] +int(i))
        number = 0
        num_list = []
        for i in s:
            if i != "0":
                number= (number *10) + int(i)
            num_list.append(str(number))
        print(suma)
        print(num_list)
        res = []
        # 1 1 3 3 6 6 6 10
        # 1 1 12 12 123 123 123 1234
        for i, j in queries:
            mul = suma[ j +1 ] -suma[i]
            add = 0
            if i == 0:
                add =num_list[j]
            else:
                prev_len = len(num_list[j - 1])
                print(prev_len)
                add = num_list[j][prev_len - 1:]
            print(mul, int(add))
            res.append((mul * int(add)) % (10 ** 9 + 7))
        return res
