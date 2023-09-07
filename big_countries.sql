/* Write your T-SQL query statement below */

/*
A country is big if:
it has an area of at least three million (i.e., 3000000 km2), or
it has a population of at least twenty-five million (i.e., 25000000).
Write a solution to find the name, population, and area of the big countries.
*/

select World.name, World.population, World.area from World
where World.area >= 3000000 or World.population >= 25000000