/* Write your T-SQL query statement below */

select distinct SalesPerson.name from SalesPerson where SalesPerson.sales_id not in
(select sales_id from Orders where com_id in 
(select com_id from Company where Company.name = 'RED'))
