
class Solution:
    def int_digits(self, num :int )- >list[int]:
        rslt = []
        while 0 < num:
            rslt.append(nu m %10)
            nu m// =10
        return rslt

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        if len(digits) < 3: # if less digits than 34, return []
            return []

        if any(i % 2 == 0 for i in digits) == False: # if there is no even value then return []. early exits.
            return []

        rslt = []
        digits = Counter(digits)

        for i in range(100, 1000, 2):
            val_to_check = Counter(self.int_digits(i))
            # val_to_check = Counter(map(int, str(i)))

            if all(digits[key] >= val_to_check[key] for key in val_to_check.keys()):
                rslt.append(i)

        return rslt




