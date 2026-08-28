/*
Write a solution to find all customers who never order anything.
Return the result table in any order.
The result format is in the following example.
*/
select Customers.name as "Customers" from Customers
where not exists
(select id from Orders
where Orders.customerId = Customers.Id)
