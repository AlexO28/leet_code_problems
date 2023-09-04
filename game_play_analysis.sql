--Write a solution to find the first login date for each player.

/* Write your T-SQL query statement below */

select player_id, min(event_date) as first_login from Activity group by player_id
