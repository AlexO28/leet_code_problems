/*
You are given a 0-indexed 2D integer array brackets where brackets[i] = [upperi, percenti] means that the ith tax bracket has an upper bound of upperi and is taxed at a rate of percenti. The brackets are sorted by upper bound (i.e. upperi-1 < upperi for 0 < i < brackets.length).
Tax is calculated as follows:
The first upper0 dollars earned are taxed at a rate of percent0.
The next upper1 - upper0 dollars earned are taxed at a rate of percent1.
The next upper2 - upper1 dollars earned are taxed at a rate of percent2.
And so on.
You are given an integer income representing the amount of money you earned. Return the amount of money that you have to pay in taxes. Answers within 10-5 of the actual answer will be accepted.
*/
public class Solution {
    public double CalculateTax(int[][] brackets, int income) {
        double res = 0;
        int pos = 0;
        int prev_num = 0;
        while (income > 0) {
            int temp = brackets[pos][0] - prev_num;
            if (income > temp) {
                income -= temp;
                res += temp * brackets[pos][1] / 100.0;
            } else {
                res += income * brackets[pos][1] / 100.0;
                income = 0;
            }
            if (pos < brackets.Length) {
                prev_num = brackets[pos][0];
                ++pos;
            }
        }
        return res;
    }
}
