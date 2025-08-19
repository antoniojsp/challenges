
# Write your MySQL query statement below
SELECT u.name as name, SUM(t.amount) as balance from Transactions AS t
LEFT JOIN Users AS u ON t.account = u.account
GROUP BY u.account
HAVING balance > 10000
ORDER BY balance DESC

