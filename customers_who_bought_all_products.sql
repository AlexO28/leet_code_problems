--Write a solution to report the customer ids from the Customer table that bought all the products in the Product table.

/* Write your T-SQL query statement below */

with info as 
(select customer_id, count(distinct product_key) as cnt from
(select customer_id, product_key from Customer
where product_key in (select product_key from Product)) as A
group by customer_id)
select customer_id from info 
where cnt in (select count(distinct product_key) as max_num from Product)
