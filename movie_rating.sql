/* Write a solution to:

Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.

*/

/* Write your T-SQL query statement below */

with grouped_ratings as
(select user_id, count(movie_id) as cnt from MovieRating
group by user_id),
max_ratings as
(select max(cnt) as cnt from grouped_ratings),
filtered_ratings as
(select user_id from grouped_ratings inner join max_ratings
on grouped_ratings.cnt = max_ratings.cnt),
query_1 as
(select top 1 Users.name as results from Users inner join filtered_ratings
on Users.user_id = filtered_ratings.user_id order by Users.name),
movie_ratings as
(select movie_id, avg(cast(rating as float)) as rating from MovieRating
where created_at >= '2020-02-01' and created_at <= '2020-02-29'
group by movie_id),
max_movie_ratings as
(select max(rating) as rating from movie_ratings),
filtered_movie_ratings as
(select movie_id from movie_ratings inner join max_movie_ratings
on movie_ratings.rating = max_movie_ratings.rating),
query_2 as
(select top 1 title as results from Movies inner join filtered_movie_ratings
on Movies.movie_id = filtered_movie_ratings.movie_id
order by title)
(select * from query_1) union all (select * from query_2)
