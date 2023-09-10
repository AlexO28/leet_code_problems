--Write a solution to find all the authors that viewed at least one of their own articles.

/* Write your T-SQL query statement below */

select distinct A.author_id as id from Views as A inner join Views as B
on A.author_id = B.viewer_id and A.article_id = B.article_id
order by id
