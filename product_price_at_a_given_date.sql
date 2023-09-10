--Write an SQL query to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.

/* Write your T-SQL query statement below */

with A as
(select * from Products where change_date <= '2019-08-16'),
changed_tab as
(select A.product_id, first_value(A.new_price) over (partition by A.product_id order by A.change_date desc) as price
from  A)
(select * from changed_tab) union
(select product_id, 10 as price from Products where not exists
(select A.product_id from A where A.product_id = Products.product_id))
