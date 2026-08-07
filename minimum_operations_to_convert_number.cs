/* You are given a 0-indexed integer array nums containing distinct numbers, an integer start, and an integer goal. There is an integer x that is initially set to start, and you want to perform operations on x such that it is converted to goal. You can perform the following operation repeatedly on the number x:
If 0 <= x <= 1000, then for any index i in the array (0 <= i < nums.length), you can set x to any of the following:
x + nums[i]
x - nums[i]
x ^ nums[i] (bitwise-XOR)
Note that you can use each nums[i] any number of times in any order. Operations that set x to be out of the range 0 <= x <= 1000 are valid, but no more operations can be done afterward.
Return the minimum number of operations needed to convert x = start into goal, and -1 if it is not possible. */
using System;
using System.Collections.Generic;


public class Solution {
    public int MinimumOperations(int[] nums, int start, int goal) {
        Func<int, int, int> op1 = (x, y) => x + y;
        Func<int, int, int> op2 = (x, y) => x - y;
        Func<int, int, int> op3 = (x, y) => x ^ y;
        Func<int, int, int>[] ops = new Func<int, int, int>[] {op1, op2, op3};
        bool[] vis = new bool[1001];
        LinkedList<(int X, int Y)> q = new LinkedList<(int, int)>();
        q.AddLast((start, 0));
        while (q.Count > 0) {
            (int x, int step) = q.First.Value;
            q.RemoveFirst(); 
            int nextStep = step + 1;
            foreach (int num in nums) {
                foreach (Func<int, int, int> op in ops) {
                    int nx = op(x, num);
                    if (nx == goal) {
                        return nextStep;
                    } else if ((0 <= nx) && (nx <= 1000) && (!vis[nx])) {
                        q.AddLast((nx, nextStep));
                        vis[nx] = true;
                    }
                }
            }
        }
        return -1;
    }
}
