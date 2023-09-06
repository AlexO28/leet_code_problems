# Write a solution to report the sum of all total investment values in 2016 tiv_2016, for all policyholders who:
# have the same tiv_2015 value as one or more other policyholders, and
#are not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).
#Round tiv_2016 to two decimal places.

with A as
(select A.pid from Insurance as A inner join Insurance as B
on A.pid != B.pid and A.tiv_2015 = B.tiv_2015),
B as
(select pid from Insurance where concat(lat, lon) in (
select D.city from
(select C.city, count(*) as cnt from
(select concat(lat, lon) as city from Insurance) as C
group by C.city) as D
where D.cnt = 1))
select round(sum(tiv_2016), 2) as tiv_2016 from Insurance where Insurance.pid in
(select A.pid from A inner join B
on A.pid = B.pid)
