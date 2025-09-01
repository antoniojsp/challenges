
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        suma = sum(arr)
        if suma%3 != 0: # if total sum from arr cannot be devided exactly by 3, then return False (no way to create 3 equally sized partitions)
            return False

        curr_sum = 0
        count = 0
        avg = suma//3
        for val in arr:
            curr_sum+=val
            if curr_sum == avg:
                curr_sum = 0
                count+=1


        return count >= 3