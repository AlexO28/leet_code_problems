--Write a solution to report the latest login for all users in the year 2020. Do not include the users who did not login in 2020.

/* Write your T-SQL query statement below */

select A.user_id, max(A.time_stamp) as last_stamp from
(select * from Logins
where (time_stamp >= '2020-01-01 00:00:00') and (time_stamp <= '2020-12-31 23:59:59')) as A
group by A.user_id
