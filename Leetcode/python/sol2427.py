
# https://leetcode.com/problems/number-of-common-factors/description/


def commonFactors(a: int, b: int) -> int:
    return max(i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0)


a = 4
b = 5
print(commonFactors(a,b))
print(abs(a*b)//commonFactors(a,b))