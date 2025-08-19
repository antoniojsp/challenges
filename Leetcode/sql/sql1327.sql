# https://leetcode.com/problems/list-the-products-ordered-in-a-period/

# Write your MySQL query statement below

SELECT product_name, SUM(UNIT) as unit FROM Products AS p
LEFT JOIN Orders AS o ON p.product_id = o.product_id
WHERE YEAR(o.order_date) = 2020 AND MONTH(o.order_date) = 02
GROUP BY p.product_id
HAVING unit >= 100

