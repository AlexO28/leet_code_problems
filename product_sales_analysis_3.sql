--Write a solution to select the product id, year, quantity, and price for the first year of every product sold.

# Write your MySQL query statement below

select product_id, year as first_year, quantity, price from Sales
    where (product_id, year) in (
        select product_id, min(year) from Sales
        group by product_id)
