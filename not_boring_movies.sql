/* Write a solution to report the movies with an odd-numbered ID and a description that is not "boring".
Return the result table ordered by rating in descending order.*/

/* Write your T-SQL query statement below */

select * from Cinema
where Cinema.id % 2 = 1 and Cinema.description != 'boring'
order by Cinema.rating desc
