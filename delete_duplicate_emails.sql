/*
Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.
For Pandas users, please note that you are supposed to modify Person in place.
After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.
The result format is in the following example.
*/
delete from Person
from Person as A
where exists
(select * from
(select B.email, min(B.id) as id from Person as B
group by B.email
having count(B.id) > 1) as C
where A.email = C.email and A.id > C.id)
