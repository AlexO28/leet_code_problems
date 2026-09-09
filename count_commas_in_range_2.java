/*
You are given an integer n.
Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.
In standard formatting:
A comma is inserted after every three digits from the right.
Numbers with fewer than 4 digits contain no commas.
*/
class Solution {
    public long countCommas(long n) {
        long numberOfCommas = 0;
        String nStr = String.valueOf(n);
        if (nStr.length() < 4) {
            return numberOfCommas;
        }
        long num = 1;
        for (int i = 2; i < nStr.length(); i += 3) {
            num *= 1000;
            if ((num < 0) || (num > n)) {
                break;
            }
            numberOfCommas += n - num + 1; 
        }
        return numberOfCommas;
    }
}
