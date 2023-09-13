--Write a solution to get the names of products that have at least 100 units ordered in February 2020 and their amount.

/* Write your T-SQL query statement below */

select Products.product_name, A.unit from Products inner join
(select product_id, sum(unit) as unit from Orders
where order_date >= '2020-02-01' and order_date <= '2020-02-29'
group by product_id
having sum(unit) >= 100) as A
on Products.product_id = A.product_id
