--Write a solution to find the number of times each student attended each exam.

/* Write your T-SQL query statement below */

select B.student_id, B.student_name, B.subject_name,
case when A.attended_exams is null then 0 else A.attended_exams end as attended_exams 
from (select * from Students cross join Subjects) as B
left join
(select student_id, subject_name, count(1) as attended_exams from Examinations group by student_id, subject_name) as A
on B.student_id = A.student_id and B.subject_name = A.subject_name
order by B.student_id, B.subject_name
