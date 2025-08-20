
# https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/?source=submission-noac

# Write your MySQL query statement below

SELECT customer_number FROM Orders o
GROUP BY customer_number
HAVING COUNT(customer_number)
ORDER BY COUNT(customer_number) DESC
LIMIT 1