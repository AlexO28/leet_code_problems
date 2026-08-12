/*
A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.
For example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively, which read the same both forward and backward.
On the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 100, which does not read the same both forward and backward.
Given the base k and the number n, return the sum of the n smallest k-mirror numbers.
*/
using System;
using System.Collections.Generic;


public class Solution {
    public long KMirror(int k, int n) {
        long res = 0;
        for (int l = 1; ; ++l) {
            int x = (int) Math.Pow(10, (l - 1) / 2);
            int y = (int) Math.Pow(10, (l + 1) / 2);
            for (int i = x; i < y; ++i) {
                long v = i;
                int j = (l % 2 == 0) ? i : i / 10;
                while (j > 0) {
                    v = v * 10 + j % 10;
                    j /= 10;
                }
                if (check(v, k)) {
                    res += v;
                    if (--n == 0) {
                        return res;
                    }
                }
            }
        }
    }

    private bool check(long x, int k) {
        List<int> s = new List<int>();
        while (x > 0) {
            (x, long remainder) = Math.DivRem(x, k);
            s.Add((int) (remainder));
        }
        for (int i = 0, j = s.Count - 1; i < j; ++i, --j) {
            if (s[i] != s[j]) {
                return false;
            }
        }
        return true;
    }
}
