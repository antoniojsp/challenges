
# https://leetcode.com/problems/sales-person/
-- # Write your MySQL query statement below

SELECT name FROM SalesPerson
WHERE  sales_id NOT IN (
    SELECT o.sales_id FROM orders o
                    WHERE com_id IN (SELECT com_id FROM Company
                                        WHERE name = "RED")
)



