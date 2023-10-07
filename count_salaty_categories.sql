/*Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:
"Low Salary": All the salaries strictly less than $20000.
"Average Salary": All the salaries in the inclusive range [$20000, $50000].
"High Salary": All the salaries strictly greater than $50000.*/

/* Write your T-SQL query statement below */
(select 'Low Salary' as category, count(account_id) as accounts_count from Accounts where income < 20000) union
(select 'Average Salary' as category, count(account_id) as accounts_count from Accounts where income >= 20000 and income <= 50000) union
(select 'High Salary' as category, count(account_id) as accounts_count from Accounts where income > 50000)
