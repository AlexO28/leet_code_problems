/*
You are given an integer total indicating the amount of money you have. You are also given two integers cost1 and cost2 indicating the price of a pen and pencil respectively. You can spend part or all of your money to buy multiple quantities (or none) of each kind of writing utensil.
Return the number of distinct ways you can buy some number of pens and pencils.
*/
class Solution {
    public long waysToBuyPensPencils(int total, int cost1, int cost2) {
        long number_of_ways = 0;
        for (int number_of_pencils = 0; number_of_pencils <= total; ++number_of_pencils) {
            int delta = total - number_of_pencils * cost1;
            if (delta < 0) {
                break;
            } else {
                number_of_ways += delta / cost2 + 1;
            }
        }
        return number_of_ways;
    }
}
