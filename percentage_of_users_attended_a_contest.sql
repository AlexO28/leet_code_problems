--Write a solution to find the percentage of the users registered in each contest rounded to two decimals.


select * from
(select contest_id, round(100* cast(count(user_id) as float)/(select cast(count(distinct user_id) as float) from Users), 2) as [percentage] from Register group by contest_id) as A
order by [percentage] desc, contest_id asc
