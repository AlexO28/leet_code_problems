/*
The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested confirmation messages. The confirmation rate of a user that did not request any confirmation messages is 0. Round the confirmation rate to two decimal places.

Write a solution to find the confirmation rate of each user.
*/

/* Write your T-SQL query statement below */

with C as
(select A.user_id,
isnull(round(cast(cnt2 as float)/(cnt1 + 0.0000001), 2), 0) as confirmation_rate
from
(select Confirmations.user_id, count(time_stamp) as cnt1 from Confirmations group by Confirmations.user_id) as A
left join
(select Confirmations.user_id, count(time_stamp) as cnt2 from Confirmations
where Confirmations.action = 'confirmed' group by Confirmations.user_id) as B
on A.user_id = B.user_id)
(select Signups.user_id, 0 as confirmation_rate from Signups
where not exists
(select C.user_id from C where C.user_id = Signups.user_id))
union
(select * from C)
