/*
You are given a 0-indexed 2D integer array tires where tires[i] = [fi, ri] indicates that the ith tire can finish its xth successive lap in fi * ri(x-1) seconds.
You are also given an integer changeTime and an integer numLaps.
The race consists of numLaps laps and you may start the race with any tire. You have an unlimited supply of each tire and after every lap, you may change to any given tire (including the current tire type) if you wait changeTime seconds.
Return the minimum time to finish the race.
*/
import java.util.Arrays;


class Solution {
    public int minimumFinishTime(int[][] tires, int changeTime, int numLaps) {
        final int inf = 1 << 30;
        int[] cost = new int[18];
        Arrays.fill(cost, inf);
        for (int[] e : tires) {
            int f = e[0];
            int r = e[1];
            int s = 0;
            int t = f;
            int nextTime = changeTime + f;
            for (int i = 1; t <= nextTime; ++i) {
                s += t;
                cost[i] = Math.min(cost[i], s);
                t *= r;
            }
        }
        int[] f = new int[numLaps + 1];
        Arrays.fill(f, inf);
        f[0] = -changeTime;
        for (int i = 1; i <= numLaps; ++i) {
            int upperLimit = Math.min(18, i + 1);
            for (int j = 1; j < upperLimit; ++j) {
                f[i] = Math.min(f[i], f[i - j] + cost[j]);
            }
            f[i] += changeTime;
        }
        return f[numLaps];
    }
}
