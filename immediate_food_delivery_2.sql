/*If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.

Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.*/

/* Write your T-SQL query statement below */

select 
round(100  *
(select cast(count(distinct Delivery.customer_id) as float) from Delivery inner join
(select customer_id, min(order_date) over (partition by customer_id) as min_date from Delivery) as A
on Delivery.customer_id = A.customer_id and Delivery.order_date = A.min_date
where Delivery.order_date = Delivery.customer_pref_delivery_date) / 
(select cast(count(distinct customer_id) as float) from Delivery), 2) as immediate_percentage
