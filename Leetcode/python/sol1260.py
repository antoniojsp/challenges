# https://leetcode.com/problems/shift-2d-grid/description/
def unflatten(arr:List[int], len_row:int):
    return [arr[i:i+len_row] for i in range(0,len(arr), len_row)]

def flatten(arr:List[int]):
    oneDim = []
    for i in arr:
        oneDim.extend(i)
    return oneDim

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        oneDim = flatten(grid)
        shifted = [0]*len(oneDim)
        for i in range(len(oneDim)):
            index = (i + k)%len(oneDim)
            shifted[index] = oneDim[i]
        len_row =len(grid[0])
        return unflatten(shifted, len_row)

