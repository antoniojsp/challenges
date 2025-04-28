#
class Solution:
    def countSeniors(self, details: List[str]) -> int:

        count_seniors = 0
        for i in details:
            if int(i[11:13]) > 60:
                count_seniors+=1

        return count_seniors