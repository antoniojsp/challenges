# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/description/
class Solution:
    def __init__(self):
        self.board = ["" ] *9
        self.player = "A"

    def check_winner(self):
        winners = [(0 ,1 ,2),
                   (3 ,4 ,5),
                   (6 ,7 ,8),
                   (0 ,3 ,6),
                   (1 ,4 ,7),
                   (2 ,5 ,8),
                   (0 ,4 ,8),
                   (2 ,4 ,6)]

        for a ,b ,c in winners:
            if self.board[a] != "" and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def tictactoe(self, moves: List[List[int]]) -> str:
        isWinner = None
        for i, j in moves:
            self.board[ i * 3 +j] = self.player
            self.player = "A" if self.player == "B" else "B"
            isWinner = self.check_winner()
            if isWinner:
                return isWinner
        return "Pending" if len(moves) < 9  else "Draw"
