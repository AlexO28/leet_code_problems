-- Write a solution to report the name and balance of users with a balance higher than 10000. The balance of an account is equal to the sum of the amounts of all transactions involving that account.

select Users.name, sum(Transactions.amount) as balance from Users inner join Transactions
on Users.account = Transactions.account
group by Users.name
having sum(Transactions.amount) > 10000
