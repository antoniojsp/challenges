import unittest

test_cases = [
    # true="Mr John Smith" (len=13, spaces=2) → expected len=13+2*2=17; input len=17 ✓
    ("Mr John Smith    ", 13, "Mr%20John%20Smith"),

    # true="NoSpacesHere" (len=12, spaces=0) → expected len=12; input len=12 ✓
    ("NoSpacesHere", 12, "NoSpacesHere"),

    # true=" LeadingSpace" (len=13, spaces=1) → expected len=13+2=15; input len=15 ✓
    (" LeadingSpace  ", 13, "%20LeadingSpace"),

    # true="Trailing space" (len=14, spaces=1) → expected len=14+2=16; input len=17 ✓
    ("Trailing space  ", 14, "Trailing%20space"),

    # true="Multiple  spaces here" (len=21, spaces=3) → expected len=21+6=27; input len=27 ✓
    ("Multiple  spaces here      ", 21, "Multiple%20%20spaces%20here"),

    # true="  " (first 2 spaces) (len=2, spaces=2) → expected len=2+4=6; input len=6 ✓
    ("      ", 2, "%20%20"),

    # true="" (len=0, spaces=0) → expected len=0; input len=0 ✓
    ("", 0, ""),

    # true="SingleSpace " (len=12, spaces=1) → expected len=12+2=14; input len=14 ✓
    ("SingleSpace   ", 12, "SingleSpace%20"),

    # true="a b c" (len=5, spaces=2) → expected len=5+4=9; input len=9 ✓
    ("a b c    ", 5, "a%20b%20c"),

    # true="EndsWithTwoSpaces  " (len=19, spaces=2) → expected len=19+4=23; input len=23 ✓
    ("EndsWithTwoSpaces      ", 19, "EndsWithTwoSpaces%20%20"),
]


def urlify(input_str, true_length) -> str:

    char_list = list(input_str)
    white_spaces = char_list[:true_length].count(' ')
    end = true_length + (white_spaces*2) -1# the end of the total
    start_rewriting = true_length - 1 # where string is starts
    while 0 <= start_rewriting:
        if char_list[start_rewriting] == ' ':
            char_list[end-2:end+1] = "%20"
            end-=3
        else:
            char_list[end] = char_list[start_rewriting]
            end-=1
        start_rewriting -= 1

    return "".join(char_list)


class TestURLify(unittest.TestCase):
    def test_urlify(self):
        for input_str, true_length, expected in test_cases:
            self.assertEqual(urlify(input_str, true_length), expected)


if __name__ == '__main__':
    unittest.main()
