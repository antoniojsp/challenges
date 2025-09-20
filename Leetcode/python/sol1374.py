    # # https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/description/
    #
    #
    # class Solution:
    #     def generateTheString(self, n: int) -> str:
    #         return "a"+"b"*(n-1) if n%2 == 0 else "a"*n
    #


grid = [[' ' for _ in range(19)] for _ in range(8)]
def place(x, y, label):
    i_x = int(x) + 6
    i_y = 7 - int(y)
    grid[i_y][i_x] = label
place(0,6, 'B')
place(12,5, '3')
place(5,2, '1')
place(-3,2, '5')
place(0,1, '2')
place(0,0, 'D')
place(5,0, 'S')
place(-5,0, '4')
for row in grid:
    print(''.join(row))
print('Columns represent X from -6 to 12 ft, rows Y from 7 (top) to 0 (bottom)')
print('B: bed, D: door, S: shelves, 1-5: boxes')