--Write a solution to find the ids of products that are both low fat and recyclable.

/* Write your T-SQL query statement below */

select product_id from Products where
low_fats = 'Y' and recyclable = 'Y' 
