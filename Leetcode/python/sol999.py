# https://leetcode.com/problems/available-captures-for-rook/

class Solution:
    def find_rook_pos(self, board: List[List[str]]) -> (int, int):
        size = len(board)
        for row in range(size):
            for col in range(size):
                if board[row][col] == "R":
                    return (row, col)

    def get_row_col(self, board, r_idx, c_idx) -> (List[int], List[int]):
        col = []
        for row in board:
            col.append(row[c_idx])
        return board[r_idx], col

    def check_pawn(self, arr: list, start: int):
        count = 0
        # left
        for i in range(start, len(arr)):
            if arr[i] == 'p':
                count += 1
                break
            elif arr[i] == 'B':
                break
        # right
        for i in range(start, -1, -1):
            if arr[i] == 'p':
                count += 1
                break
            elif arr[i] == 'B':
                break

        return count

    def numRookCaptures(self, board: List[List[str]]) -> int:
        row_idx, col_idx = self.find_rook_pos(board)
        row, col = self.get_row_col(board, row_idx, col_idx)
        return self.check_pawn(row, row_idx) + self.check_pawn(col, col_idx)


