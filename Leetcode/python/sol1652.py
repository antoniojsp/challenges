# https://leetcode.com/problems/defuse-the-bomb/description/
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = []
        for i in range(0 ,len(code)):
            current = i
            temp = 0
            for _ in range(abs(k)):
                if k< 0:  # go left
                    current -= 1
                    current = current % len(code)
                    temp += code[current]
                else:  # go right
                    current += 1
                    current = current % len(code)
                    temp += code[current]
            ans.append(temp)
        return ans







