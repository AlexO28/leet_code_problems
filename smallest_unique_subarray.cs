/*
You are given an integer array nums.
Find the minimum length of a subarray that is not identical to any other subarray in nums.
Return an integer denoting the minimum possible length of such a subarray.
Two subarrays are considered identical if they have the same length and the same elements in corresponding positions.
*/
using System;
using System.Collections.Generic;


public class Solution {
    private int[] nums;
    private long[] powers;

    public int SmallestUniqueSubarray(int[] nums) {
        this.powers = new long[nums.Length + 1];
        for (int i = 0; i < this.powers.Length; ++i) {
            this.powers[i] = 1;
        }
        this.nums = nums;
        int minPossibleLen = nums.Length;
        int minLen = 1;
        int maxLen = nums.Length;
        while (minLen <= maxLen) {
            int midLen = (minLen + maxLen) / 2;
            if (this.CheckUniqueness(midLen)) {
                minPossibleLen = Math.Min(minPossibleLen, midLen);
                maxLen = midLen - 1;
            } else {
                minLen = midLen + 1;
            }
        }
        return minPossibleLen;
    }

    private bool CheckUniqueness(int midLen) {
        this.powers[0] = 1;
        for (int idx = 1; idx <= this.nums.Length; ++idx) {
            this.powers[idx] = (this.powers[idx - 1] * 19) % 1000000007;
        }
        long currentHash = 0;
        for (int idx = 0; idx < midLen; ++idx) {
            currentHash *= 19;
            currentHash += this.nums[idx];
            currentHash %= 1000000007;
        }
        Dictionary<long, int> counts = new Dictionary<long, int>();
        counts[currentHash] = 1;
        for (int idx = 1; idx <= nums.Length - midLen; ++idx) {
            currentHash = ((((currentHash - this.powers[midLen - 1] * this.nums[idx - 1]) * 19) + this.nums[idx + midLen - 1]) % 1000000007);
            if (currentHash < 0) {
                currentHash += 1000000007;
            }
            if (counts.ContainsKey(currentHash)) {
                counts[currentHash] += 1;
            } else {
                counts[currentHash] = 1;
            }
        }
        return counts.ContainsValue(1);
    }
}
