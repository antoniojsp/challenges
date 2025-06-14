# https://leetcode.com/problems/lemonade-change/description/
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change :dict[int, int] = {5 :0, 10 :0}
        for bill in bills:
            match bill:
                case 5:
                    change[bill ]+ =1
                case 10:
                    if change[5] > 0:
                        change[5 ]- =1
                        change[10 ]+ =1
                    else:
                        return False
                case 20:
                    change_needed = 15
                    if change[10] > 0:
                        change_neede d- =10
                        change[10 ]- =1
                    num_fives = change_neede d/ /5
                    if change[5] >= num_fives:
                        change[5 ]- =num_fives
                    else:
                        return False
        return True



