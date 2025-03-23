class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:

        x, y = 0, 0

        for i in commands:
            match i:
                case "UP":
                    x -= 1
                case "DOWN":
                    x += 1
                case "LEFT":
                    y -= 1
                case "RIGHT":
                    y += 1

        return n * x + y
