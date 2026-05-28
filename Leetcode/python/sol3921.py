# https://leetcode.com/problems/score-validator/description/

class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        counter = 0
        for i in events:
            if counter >= 10:
                break
            if i.isdigit():
                score+=int(i)
            elif i == "W":
                counter+=1
            else:
                score+=1
        return [score, counter]
