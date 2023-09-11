--Reformat the table such that there is a department id column and a revenue column for each month.

/* Write your T-SQL query statement below */

select id,
sum(case when Department.month = 'Jan' then revenue end) as Jan_Revenue,
sum(case when Department.month = 'Feb' then revenue end) as Feb_Revenue,
sum(case when Department.month = 'Mar' then revenue end) as Mar_Revenue,
sum(case when Department.month = 'Apr' then revenue end) as Apr_Revenue,
sum(case when Department.month = 'May' then revenue end) as May_Revenue,
sum(case when Department.month = 'Jun' then revenue end) as Jun_Revenue,
sum(case when Department.month = 'Jul' then revenue end) as Jul_Revenue,
sum(case when Department.month = 'Aug' then revenue end) as Aug_Revenue,
sum(case when Department.month = 'Sep' then revenue end) as Sep_Revenue,
sum(case when Department.month = 'Oct' then revenue end) as Oct_Revenue,
sum(case when Department.month = 'Nov' then revenue end) as Nov_Revenue,
sum(case when Department.month = 'Dec' then revenue end) as Dec_Revenue
from Department group by id
