# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        line = deque(students)
        sandwiches = deque(sandwiches)
        while line:
            student = line.popleft()
            if student == sandwiches[0]:
                sandwiches.popleft()
            else:
                line.append(student)
                if sum(line) == 0 or sum(line) == len(line):
                    break
        return len(line)

