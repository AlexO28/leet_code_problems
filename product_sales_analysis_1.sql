--Write a solution to report the product_name, year, and price for each sale_id in the Sales table.

/* Write your T-SQL query statement below */

select product_name, year, price from Sales as A inner join Product as B
on A.product_id = B.product_id
