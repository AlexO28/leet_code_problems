/*
Write a solution to find the users who have valid emails.
A valid e-mail has a prefix name and a domain where:
The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. The prefix name must start with a letter.
The domain must be exactly '@leetcode.com' in lowercase.
Return the result table in any order.
The result format is in the following example.
*/
select *
from Users
where mail like '%@leetcode.com' collate Latin1_General_BIN
and patindex('[a-zA-Z]%', mail) = 1
and patindex('%[^a-zA-Z0-9_.-]%@leetcode.com', mail) = 0
