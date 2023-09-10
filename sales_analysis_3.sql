--Write a solution to report the products that were only sold in the first quarter of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.

/* Write your T-SQL query statement below */

select Product.product_id, Product.product_name from Product
where not exists
(select product_id from Sales where
(Sales.sale_date < '2019-01-01' or Sales.sale_date > '2019-03-31')
and Product.product_id = Sales.product_id
)
and exists
(select product_id from Sales
where
Product.product_id = Sales.product_id)
