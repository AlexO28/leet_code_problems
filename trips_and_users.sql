# The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

# Write a solution to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal point

with B as
(select id, request_at,
  (case when Trips.status = 'completed' then 1 else 0 end) as status_new
  from Trips where 
  (request_at = '2013-10-01' or
  request_at = '2013-10-02' or
  request_at = '2013-10-03') and
  id not in
((select id from Trips inner join
(select users_id from Users where banned = 'Yes' and Users.role = 'client') as A
on Trips.client_id = A.users_id)
union
(select id from Trips inner join
(select users_id from Users where banned = 'Yes' and Users.role = 'driver') as A
on Trips.driver_id = A.users_id)))
select
C.request_at as "Day",
case when D.cnt is not null
then round(cast(D.cnt as float)/cast(C.cnt as float), 2)
else 0 end
as "Cancellation Rate"
from
(select count(id) as cnt, request_at from B group by request_at) as C
left join
(select count(id) as cnt, request_at from B where status_new = 0 group by request_at) as D
on C.request_at = D.request_at
