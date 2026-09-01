/*
Write a solution to find all customers who never order anything.
Return the result table in any order.
*/
select "name" as "Customers" from Customers
where not exists
(select * from Orders
where Orders.customerId = Customers.id)
