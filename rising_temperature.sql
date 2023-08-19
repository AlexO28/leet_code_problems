/*Find all dates' Id with higher temperatures compared to its previous dates (yesterday).*/

select A.id as Id from Weather as A inner join Weather as B
on A.recordDate = DATEADD(day, 1, B.recordDate)
where A.temperature > B.temperature
