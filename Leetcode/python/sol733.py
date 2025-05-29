# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        S = [(sr, sc)]
        m = len(image[0])  # col
        n = len(image)  # rows
        original = image[sr][sc]
        seen = set()
        while S:
            row, col = S.pop(0)
            if image[row][col] == original:
                image[row][col] = color
            else:
                continue
            if (row, col) in seen:
                continue
            seen.add((row, col))
            # up
            if row - 1 >= 0:
                S.append((row - 1, col))
            # down
            if row + 1 < n:
                S.append((row + 1, col))
            # left
            if col - 1 >= 0:
                S.append((row, col - 1))
            # right
            if col + 1 < m:
                S.append((row, col + 1))

        return image

