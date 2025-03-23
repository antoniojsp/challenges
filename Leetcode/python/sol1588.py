class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        length = len(arr)
        odd_len = 1
        suma = 0
        while odd_len <= length:
            for i in range(0, len(arr)-odd_len+1):
                if i+odd_len <= length:
                    suma += sum(arr[i:i+odd_len])
            odd_len+=2

        return suma
