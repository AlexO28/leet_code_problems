/* We define query quality as:

The average of the ratio between query rating and its position.

We also define poor query percentage as:

The percentage of all queries with rating less than 3.

Write a solution to find each query_name, the quality and poor_query_percentage.*/

# Write your MySQL query statement below

select query_name,
    round(avg(rating/position), 2) as quality,
    round(sum(if(rating < 3, 1, 0)) / count(*) * 100, 2) as poor_query_percentage
    from Queries
    group by query_name
