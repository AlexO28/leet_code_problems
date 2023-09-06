-- Write a solution to find managers with at least five direct reports.

select Employee.name from Employee where Employee.id in
(select managerId from
(select A.managerId, count(B.id) as cnt from Employee as A inner join Employee as B on A.managerId = B.id group by A.managerId) as C where C.cnt >= 5)
