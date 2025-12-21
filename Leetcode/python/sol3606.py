
# https://leetcode.com/problems/coupon-code-validator/description/

from string import ascii_letters, digits

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        fields = defaultdict(list)
        rubros = ["electronics", "grocery", "pharmacy", "restaurant"]
        valid_fields = set(rubros)
        valid_chars = ascii_letters + digits + "_"
        for c, b, is_active in zip(code, businessLine, isActive):
            if c and b in valid_fields and is_active and all(i in valid_chars for i in c):
                fields[b].append(c)
        result = []
        for i in rubros:
            fields[i].sort()
            result.extend(fields[i])
        return result