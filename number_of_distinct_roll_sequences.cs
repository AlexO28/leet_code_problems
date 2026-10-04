# You are given an integer n. You roll a fair 6-sided dice n times. Determine the total number of distinct sequences of rolls possible such that the following conditions are satisfied:
# The greatest common divisor of any adjacent values in the sequence is equal to 1.
# There is at least a gap of 2 rolls between equal valued rolls. More formally, if the value of the ith roll is equal to the value of the jth roll, then abs(i - j) > 2.
# Return the total number of distinct sequences possible. Since the answer may be very large, return it modulo 109 + 7.
# Two sequences are considered distinct if at least one element is different.
public class Solution {
    public int DistinctSequences(int n) {
        if (n == 1) {
            return 6;
        }
        const int MOD = (int) 1000000007;
        int[,,] dp = new int[n + 1, 6, 6];
        for (int i = 0; i < 6; ++i) {
            for (int j = 0; j < 6; ++j) {
                if (gcd(i + 1, j + 1) == 1 && i != j) {
                    dp[2, i, j] = 1;
                }
            }
        }
        for (int k = 3; k <= n; ++k) {
            for (int i = 0; i < 6; ++i) {
                for (int j = 0; j < 6; ++j) {
                    if (gcd(i + 1, j + 1) == 1 && i != j) {
                        for (int h = 0; h < 6; ++h) {
                            if (gcd(h + 1, i + 1) == 1 && h != i && h != j) {
                                dp[k, i, j] = (dp[k, i, j] + dp[k - 1, h, i]) % MOD;
                            }
                        }
                    }
                }
            }
        }
        int res = 0;
        for (int i = 0; i < 6; ++i) {
            for (int j = 0; j < 6; ++j) {
                res = (res + dp[n, i, j]) % MOD;
            }
        }
        return res;
    }

    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
