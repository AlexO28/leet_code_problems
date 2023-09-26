/* Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.
Return the result table ordered by user_id. */

/* Write your T-SQL query statement below */

select user_id, concat(upper(substring(Users.name, 1, 1)), lower(substring(Users.name, 2, 255))) as [name]
from Users
order by user_id
