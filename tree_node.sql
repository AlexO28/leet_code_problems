--Write a solution to report the type of each node in the tree.

/* Write your T-SQL query statement below */

with parents as
(select id, 'Root' as type from Tree where p_id is null),
inners as
(select p_id as id, 'Inner' as type from Tree where p_id is not null and p_id not in (select id from parents)),
leaves as
(select id, 'Leaf' as type from Tree where id not in
(select id from inners) and id not in (select id from parents)
)
(select * from parents) union (select * from inners) union (select * from leaves)
