# https://leetcode.com/problems/shortest-distance-to-a-character/description/?envType=problem-list-v2&envId=string

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [float('inf')]*len(s)
        indexes = [i  for i in range(len(s)) if s[i] == c]
        for i in range(len(ans)):
            for j in indexes:
                ans[i] = min(ans[i], abs(j - i))
                if abs(j - i) == 0:
                    break
        return ans


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        pos = [i for i in range(len(s)) if s[i] == c]
        ans = [0] * len(s)
        pos_i = 0
        for i in range(len(s)):
            distance = abs(i - pos[pos_i])
            ans[i] = distance
            if distance == 0 and pos_i + 1 < len(pos):
                pos_i += 1

        pos_j = len(pos) - 1
        for i in range(len(s) - 1, -1, -1):
            distance = abs(i - pos[pos_j])
            ans[i] = min(distance, ans[i])
            if distance == 0 and 0 <= pos_j - 1:
                pos_j -= 1

        return ans




