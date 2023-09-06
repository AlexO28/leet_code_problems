-- Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.

select round((select cast(count(distinct player_id) as float) from
(select distinct Activity.player_id from Activity inner join
(select player_id, min(event_date) as min_date from Activity group by player_id) as A
on (A.player_id = Activity.player_id) and datediff(day, A.min_date, Activity.event_date) = 1) as B)/ 
(select cast(count(distinct player_id) as float) from Activity), 2) as fraction
