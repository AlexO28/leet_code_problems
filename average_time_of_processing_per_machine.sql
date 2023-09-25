/* There is a factory website that has several machines each running the same number of processes. Write a solution to find the average time each machine takes to complete a process.
The time to complete a process is the 'end' timestamp minus the 'start' timestamp. The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.
The resulting table should have the machine_id along with the average time as processing_time, which should be rounded to 3 decimal places.
*/

/* Write your T-SQL query statement below */

select machine_id, round(avg(diff), 3) as processing_time from 
(select machine_id, process_id,
max(Activity.timestamp) - min(Activity.timestamp) as diff
from Activity group by machine_id, process_id) as A
group by machine_id
