test_cases = [
    # Basic rotations
    ("waterbottle", "erbottlewat", True),  # simple rotation
    ("abcde", "cdeab", True),  # rotated in middle
    ("abcde", "deabc", True),  # rotated near end

    # Identical strings (rotation by 0)
    ("aaaa", "aaaa", True),
    ("abc", "abc", True),

    # Different lengths
    ("abc", "ab", False),
    ("", "a", False),

    # Empty strings
    ("", "", True),

    # Not rotations
    ("hello", "world", False),
    ("abcd", "acbd", False),  # permutation but not rotation
    ("waterbottle", "bottlewaterx", False),  # extra char
]

import unittest

def is_rotation(s1: str, s2: str) -> bool:
    # Hint: s2 must be a substring of s1+s1 if it's a rotation
    if len(s1) != len(s2):
        return False
    test = s1+s1
    return s2 in test


class TestStringRotation(unittest.TestCase):
    def test_is_rotation(self):
        for s1, s2, expected in test_cases:
            with self.subTest(s1=s1, s2=s2):
                self.assertEqual(is_rotation(s1, s2), expected)

if __name__ == "__main__":
    unittest.main()
