/*
You are given two positive integers left and right with left <= right. Calculate the product of all integers in the inclusive range [left, right].
Since the product may be very large, you will abbreviate it following these steps:
Count all trailing zeros in the product and remove them. Let us denote this count as C.
For example, there are 3 trailing zeros in 1000, and there are 0 trailing zeros in 546.
Denote the remaining number of digits in the product as d. If d > 10, then express the product as <pre>...<suf> where <pre> denotes the first 5 digits of the product, and <suf> denotes the last 5 digits of the product after removing all trailing zeros. If d <= 10, we keep it unchanged.
For example, we express 1234567654321 as 12345...54321, but 1234567 is represented as 1234567.
Finally, represent the product as a string "<pre>...<suf>eC".
For example, 12345678987600000 will be represented as "12345...89876e5".
Return a string denoting the abbreviated product of all integers in the inclusive range [left, right].
*/
impl Solution {
    pub fn abbreviate_product(left: i32, right: i32) -> String {
        let mut cnt2 = 0;
        let mut cnt5 = 0;
        for x in left..=right {
            let mut xx = x;
            while xx % 2 == 0 {
                cnt2 += 1;
                xx /= 2;
            }
            while xx % 5 == 0 {
                cnt5 += 1;
                xx /= 5;
            }
        }
        let c = cnt2.min(cnt5);
        let mut remove_2 = c;
        let mut remove_5 = c;
        let mut suf: i64 = 1;
        let mut prod: f64 = 1.0;
        let mut total_digits = 0;
        for x in left..=right {
            let mut xx = x as i64;           
            prod *= x as f64;
            while prod >= 1.0 {
                prod /= 10.0;
                total_digits += 1;
            }
            while remove_2 > 0 && xx % 2 == 0 {
                xx /= 2;
                remove_2 -= 1;
            }
            while remove_5 > 0 && xx % 5 == 0 {
                xx /= 5;
                remove_5 -= 1;
            }
            suf *= xx;
            if suf >= 10_000_000_000 {
                suf %= 10_000_000_000;
            }
        }
        if total_digits - c <= 10 {
            return format!("{}e{}", suf, c);
        }
        let pre = (prod * 100000.0).floor() as i64;
        format!("{}...{:05}e{}", pre, suf % 100_000, c)
    }
}
