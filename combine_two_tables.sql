/*Write a solution to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.
Return the result table in any order.*/
select A.firstName, A.lastName, B.city, B.state from Person as A
left join Address as B
on A.personId = B.personId
