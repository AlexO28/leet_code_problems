---Write a solution to find all the classes that have at least five students.

/* Write your T-SQL query statement below */

select class from 
(select class, count(student) as number_of_students from Courses group by class) as A
where number_of_students >= 5
