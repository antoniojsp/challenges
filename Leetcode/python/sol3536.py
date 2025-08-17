
class Solution:
    def digits_num(self, n :int ) ->list:
        rslt = []
        while 0 < n:
            rslt.append(n%10)
            n//=10
        return rslt

    def maxProduct(self, n: int) -> int:
        if n < 10:
            return n
        digits = self.digits_num(n)
        first = -1 # by constr  int, there are no negative values
        second = -1
        for i in digits:
            if i >= first: # if i >= f  rst, swap first and second and upadte first
                second = first
                first = i
            elif i > second: # if not, i   i > second , then update the second position
                second = i
        return first * second
