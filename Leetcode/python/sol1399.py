# https://leetcode.com/problems/count-largest-group/description/?envType=daily-question&envId=2025-04-23
class Solution:

    def sum_digits(self, nums :int) -> int:
        rslt = 0
        while 1 <= nums:
            temp = num s %10
            num s// =10
            rsl t+ =temp
        return rslt

    def countLargestGroup(self, n: int) -> int:
        sizes_values :dict = {}
        for i in range(1, n+ 1):
            suma = self.sum_digits(i)
            sizes_values[suma] = sizes_values.get(suma, 0) + 1
        greatest = max(sizes_values.values())
        return list(sizes_values.values()).count(greatest)

        # same_value_groups = {}
        # for i in range(1, n+1):
        #     suma = self.sum_digits(i)
        #     same_value_groups[suma] = same_value_groups.get(suma, [])
        #     same_value_groups[suma].append(i)

        # lenghts = {}
        # for i in same_value_groups.values():
        #     lenghts[len(i)] = lenghts.get(len(i), 0) + 1
        # return lenghts[max(lenghts.keys())]



