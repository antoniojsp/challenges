#  https://leetcode.com/problems/valid-sudoku/description/
class Solution:
    def check_row(self, line :List[str]) -> bool:
        seen = set()
        for i in line:
            if i == '.':
                continue
            if i in seen:
                return False
            seen.add(i)
        return True

    def check_column(self,  board :List[List[str]], col :int):
        seen = set()
        for row in board:
            if row[col] == '.':
                continue
            if row[col] in seen:
                return False
            seen.add(row[col])
        return True

    def check_box(self, board :List[List[str]], top_left :tuple):
        seen = set()
        length = 3
        row, col = top_left
        for i in range(row, row +length):
            for j in range(col, col +length):
                if board[i][j] == '.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            if not self.check_row(row):
                return False
        # check columns
        for col in range(len(board[0])):
            if not self.check_column(board, col):
                return False

        box_top_left = [(0 ,0), (0 ,3), (0 ,6),
                        (3 ,0), (3 ,3), (3 ,6),
                        (6 ,0), (6 ,3), (6 ,6)]

        # check box
        for i in box_top_left:
            if not self.check_box(board, i):
                return False

        return True

