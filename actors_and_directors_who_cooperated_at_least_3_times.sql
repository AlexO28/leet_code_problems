--Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.

/* Write your T-SQL query statement below */

with A as
(select actor_id, director_id, count(actor_id) as cnt from ActorDirector
group by actor_id, director_id
having count(actor_id) >= 3)
select distinct actor_id, director_id from A
