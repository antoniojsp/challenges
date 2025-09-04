test_cases = [
    ("aabcccccaaa", "a2b1c5a3"),  # typical compression
    ("abcdef", "abcdef"),          # no repeats, compression longer → return original
    ("aabbcc", "aabbcc"),          # compression same length → return original
    ("aaa", "a3"),                 # single character repeated
    ("a", "a"),                     # single character
    ("", ""),                       # empty string
    ("aaAA", "aaAA"),               # case-sensitive
    ("aabbaa", "aabbaa"),         # repeated pattern
]



import unittest

# Function to implement
def compress_string(s: str) -> str:
    # Your implementation here
    if not s:
        return ""
    current = s[0]
    count = 1
    ans = []
    for i in s[1:]:
        if current == i:
            count+=1
        else:
            ans+=[current, str(count)]
            count = 1
            current = i
    ans+=[current, str(count)]
    return s if len(s) <= len(ans) else "".join(ans)

# Unit test class
class TestStringCompression(unittest.TestCase):
    def test_compress_string(self):
        for s, expected in test_cases:
            self.assertEqual(compress_string(s), expected)

if __name__ == "__main__":
    unittest.main()