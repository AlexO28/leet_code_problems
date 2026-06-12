/*
You are given a strictly increasing integer array rungs that represents the height of rungs on a ladder. You are currently on the floor at height 0, and you want to reach the last rung.
You are also given an integer dist. You can only climb to the next highest rung if the distance between where you are currently at (the floor or on a rung) and the next rung is at most dist. You are able to insert rungs at any positive integer height if a rung is not already there.
Return the minimum number of rungs that must be added to the ladder in order for you to climb to the last rung.
*/
using System;


public class Solution {
    public int AddRungs(int[] rungs, int dist) {
        int numberOfRungs = 0;
        int prevRung = 0;
        foreach (int rung in rungs) {
            var (mainPart, remainder) = Math.DivRem(rung - prevRung, dist);
            if (remainder == 0) {
                --mainPart;
            }
            numberOfRungs += mainPart;
            prevRung = rung;
        }
        return numberOfRungs;
    }
}
