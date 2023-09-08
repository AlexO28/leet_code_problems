---Write a solution to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.

/* Write your T-SQL query statement below */

with D as
(select A.id as id1, B.id as id2, C.id as id3 from Stadium as A
inner join Stadium as B
on B.id = A.id + 1
inner join Stadium as C
on C.id = B.id + 1
where A.people >= 100 and B.people >= 100 and C.people >= 100)
select * from Stadium where id in
((select id1 from D) union
(select id2 from D) union
(select id3 from D))
