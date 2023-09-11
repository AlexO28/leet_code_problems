--Write an SQL query to find the average selling price for each product. average_price should be rounded to 2 decimal places.

/* Write your T-SQL query statement below */

select Prices.product_id, round(cast(sum(price * units) as float)/cast(sum(units) as float), 2) as average_price from Prices left join UnitsSold
on (Prices.start_date <= UnitsSold.purchase_date and 
Prices.end_date >= UnitsSold.purchase_date and Prices.product_id = UnitsSold.product_id)
group by Prices.product_id
