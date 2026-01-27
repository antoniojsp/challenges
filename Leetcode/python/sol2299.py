# https://leetcode.com/problems/strong-password-checker-ii/
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        lowercase = uppercase = digit = special = False
        ch_special = set("!@#$%^&*()-+")

        for i, val in enumerate(password):
            if val.islower():
                lowercase = True
            elif val.isupper():
                uppercase = True
            elif val.isdigit():
                digit = True
            elif val in ch_special:
                special = True

            if i + 1 < len(password) and password[i] == password[ i +1]:
                return False

        return lowercase and uppercase  and digit and special