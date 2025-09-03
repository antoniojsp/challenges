test_cases = [
    ("abc", "bca", True),                   # simple permutation
    ("abc", "abc", True),                   # identical strings
    ("abc", "abcd", False),                 # different lengths
    ("aabb", "bbaa", True),                 # repeated characters, valid permutation
    ("aabb", "abab", True),                 # repeated characters, another order
    ("aabb", "aabc", False),                # repeated characters, not permutation
    ("", "", True),                          # empty strings
    ("a", "a", True),                        # single character, same
    ("a", "b", False),                       # single character, different
    ("abcABC", "CBAcba", True),             # case-sensitive permutation
    ("abc123", "321cba", True),             # letters + numbers
    ("abc!", "!cab", True),                  # letters + special character
    ("abc", "def", False),                   # completely different
    ("a"*1000, "a"*1000, True),             # long identical strings
    ("a"*500 + "b"*500, "b"*500 + "a"*500, True),  # long strings, valid permutation
    ("a"*500 + "b"*500, "a"*1000, False)    # long strings, invalid permutation
]

import unittest
def is_permutation(str1:str, str2:str) -> bool:
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)

class Test(unittest.TestCase):
    def test_is_permutation(self):
        for str1, str2, result in test_cases:
            self.assertEqual(is_permutation(str1, str2) , result)

if __name__ == '__main__':
    unittest.main()
