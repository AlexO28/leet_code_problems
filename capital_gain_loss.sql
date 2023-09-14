--Write a solution to report the Capital gain/loss for each stock.

/* Write your T-SQL query statement below */

select stock_name,
sum(price * (case when operation = 'Sell' then 1 else -1 end)) as capital_gain_loss
from Stocks
group by stock_name
