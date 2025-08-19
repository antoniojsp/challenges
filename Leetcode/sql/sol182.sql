
# https://leetcode.com/problems/duplicate-emails/description/
# Write your MySQL query statement below
SELECT email FROM Person
GROUP BY email
HAVING COUNT(*) >= 2