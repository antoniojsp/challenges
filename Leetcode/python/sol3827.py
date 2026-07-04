# https://leetcode.com/problems/count-monobit-integers/description/


def binary_ones(bits_length:int) -> int:
    """
    Convert binary numbers that contains only "1"s to decilmal

    Args: bits_length: Number of ones in the binary number

    return: decimal representation of the binary number

    EXPERIMENTING
    """
    res = 0
    for i in range(bits_length):
        res+=2**i
    return res

class Solution:
    def countMonobit(self, n: int) -> int:
        res = 1
        binary = 1

        while binary <= n:
            binary = binary << 1 | 1
            res+=1
        return res
