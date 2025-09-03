test_cases = [
    ("abc", True),                     # all unique
    ("aabb", False),                   # repeated characters
    ("", True),                         # empty string
    ("a", True),                        # single character
    ("abcdefghijklmnopqrstuvwxyz", True),  # all lowercase letters
    ("abcABC", True),                   # case-sensitive unique
    ("112233", False),                  # numbers repeated
    ("!@#$%^&*()", True),               # special characters
    ("a"*1000, False),                  # all same character
    ("a"*500 + "b"*500, False),         # half a's, half b's
    (''.join(chr(i) for i in range(128)), True)  # all ASCII characters
]

import unittest

def is_unique(string:str) -> bool:
    '''
    "Check if a string has all unique characters using a set".
    :param string:
    :return: bool true or false if all chars are unique
    '''
    return len(string) == len(set(string))

def is_unique_nd(string:str) -> bool:
    list_string = sorted(string)
    list_string.sort()
    for i in range(len(list_string)-1):
        if list_string[i] == list_string[i+1]:
            return False
    return True

def is_unique_bit(string:str) -> bool:
    bit = 0
    # print(1 << 10)
    for i in string:
        pos = ord(i)
        if bit & (1 << pos) > 0:
            return False
        bit =  bit | (1<<pos)

    return True


class Test(unittest.TestCase):
    def test_is_unique_regular(self):
        for string, result in test_cases:
            self.assertEqual(is_unique(string) , result)
    def test_is_unique_sort(self):
        for string, result in test_cases:
            self.assertEqual(is_unique_nd(string) , result)
    def test_is_unique_bit(self):
        for string, result in test_cases:
            self.assertEqual(is_unique_bit(string) , result)

if __name__ == '__main__':
    unittest.main()
