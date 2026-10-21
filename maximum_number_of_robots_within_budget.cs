/*
You have n robots. You are given two 0-indexed integer arrays, chargeTimes and runningCosts, both of length n. The ith robot costs chargeTimes[i] units to charge and costs runningCosts[i] units to run. You are also given an integer budget.
The total cost of running k chosen robots is equal to max(chargeTimes) + k * sum(runningCosts), where max(chargeTimes) is the largest charge cost among the k robots and sum(runningCosts) is the sum of running costs among the k robots.
Return the maximum number of consecutive robots you can run such that the total cost does not exceed budget.
*/
using System;
using System.Collections.Generic;


public class Solution {
    public int MaximumRobots(int[] chargeTimes, int[] runningCosts, long budget) {
        LinkedList<int> q = new LinkedList<int>();
        int res = 0;
        long s  = 0;
        for (int left = 0, right = 0; right < chargeTimes.Length; ++right) {
            s += runningCosts[right];
            while ((q.Count > 0) && (chargeTimes[q.Last.Value] <= chargeTimes[right])) {
                q.RemoveLast();
            }
            q.AddLast(right);
            while ((q.Count > 0) && ((right - left + 1) * s + chargeTimes[q.First.Value] > budget)) {
                if (q.First.Value == left) {
                    q.RemoveFirst();
                }
                s -= runningCosts[left++];
            }
            res = Math.Max(res, right - left + 1);
        }
        return res;
    }
}
