
import unittest
from collections import Counter

# Test cases: (string1, string2, expected_result)
test_cases = [
    ("pale", "ple", True),
    ("pales", "pale", True),
    ("pale", "bale", True),
    ("pale", "bake", False),
    ("", "a", True),
    ("a", "", True),
    ("", "", True),
    ("abc", "abc", True),
    ("abc", "ab", True),
    ("abc", "abcd", True),
    ("abc", "abXc", True),
    ("abc", "aXcd", False),
]

# Function to implement
def one_away(s1: str, s2: str) -> bool:
    # Your implementation here
    count1 = Counter(s1)
    count2 = Counter(s2)
    diff1 = count1-count2
    diff2 = count2-count1
    return True if len(diff1)+len(diff2) <= 2 else False

def one_way_pointer(s1, s2):
    if abs(len(s1)-len(s2)):
        return False
    

print(one_way_pointer("pale", "ple"))
# Unit test class
# class TestOneAway(unittest.TestCase):
#     def test_one_away(self):
#         for s1, s2, expected in test_cases:
#             self.assertEqual(one_away(s1, s2), expected)
#
# if __name__ == "__main__":
#     unittest.main()
