/* Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.*/

/* Write your T-SQL query statement below */

select tweet_id from Tweets where len(content) > 15
