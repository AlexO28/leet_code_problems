--Write a solution to report the name and bonus amount of each employee with a bonus less than 1000.

/* Write your T-SQL query statement below */

select Employee.name, Bonus.bonus from Employee left join Bonus on Employee.empId = Bonus.empId where bonus < 1000 or bonus is null
