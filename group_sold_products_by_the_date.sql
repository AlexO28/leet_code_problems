/* Write a solution to find for each date the number of different products sold and their names.
The sold products names for each date should be sorted lexicographically.
Return the result table ordered by sell_date.*/

/* Write your T-SQL query statement below */

select sell_date, 
count(product) as num_sold,
string_agg(product, ',') within group (order by product) as products
from (select distinct sell_date, product from Activities) as A
group by sell_date
order by sell_date
