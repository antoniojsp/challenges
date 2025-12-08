# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/
class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = float('inf')
        max_salary = float('-inf')
        total = 0
        for i in salary:
            total += i
            if min_salary > i:
                min_salary = i
            if max_salary < i:
                max_salary = i
        return (total -min_salary -max_salary ) /(len(salary ) -2)
