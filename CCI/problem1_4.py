import unittest
from collections import Counter

# Test cases: (input string, expected result)
test_cases = [
    ("Tact Coa", True),             # "taco cat", ignoring spaces and case
    ("racecar", True),              # already a palindrome
    ("aabbcc", True),               # can form palindrome
    ("aabbc", True),                # can form "abcba"
    ("aabbcd", False),               # cannot form palindrome
    ("", True),                     # empty string
    ("a", True),                     # single character
    ("ab", False),                   # two different chars
    ("aa", True),                    # two same chars
    ("Able was I ere I saw Elba", True), # famous palindrome permutation
]

# Function to implement
def is_palindrome_permutation(s: str) -> bool:
    """Check if the string can be permuted to form a palindrome."""
    s = s.lower().replace(" ", "")
    count = Counter(s)
    result = 0
    for i in count.values():
        if i%2 != 0:
            result+=1
    return result <= 1

def is_palindrome_permutation_list(s: str) -> bool:
    if len(s) < 1:
        return True
    abc_arr = [0]*26
    s = s.lower()

    for char in s:
        if char.isalpha():
            abc_arr[ord(char) - ord('a')] += 1

    return sum(i for i in abc_arr if i%2!= 0) <= 1

# Unit test class
class TestPalindromePermutation(unittest.TestCase):
    def test_palindrome_permutation(self):
        for s, expected in test_cases:
            self.assertEqual(is_palindrome_permutation_list(s), expected)

if __name__ == "__main__":
    unittest.main()
