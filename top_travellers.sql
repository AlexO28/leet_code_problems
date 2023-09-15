--Write a solution to report the distance traveled by each user.

/* Write your T-SQL query statement below */

select Users.name, A.travelled_distance from Users inner join
(select Users.id,
case when sum(Rides.distance) is null then 0 else sum(Rides.distance) end as travelled_distance from Users left join Rides
on Users.id = Rides.user_id
group by Users.id) as A
on Users.id = A.id
order by travelled_distance desc, Users.name asc
