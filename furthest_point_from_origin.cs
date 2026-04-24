/* You are given a string moves of length n consisting only of characters 'L', 'R', and '_'. The string represents your movement on a number line starting from the origin 0.
In the ith move, you can choose one of the following directions:
move to the left if moves[i] = 'L' or moves[i] = '_'
move to the right if moves[i] = 'R' or moves[i] = '_'
Return the distance from the origin of the furthest point you can get to after n moves.
*/
using System;


public class Solution {
    public int FurthestDistanceFromOrigin(string moves) {
        int distance_1 = 0;
        int distance_2 = 0;
        foreach(char move in moves) {
            if (move == 'L') {
                distance_1 -= 1;
                distance_2 -= 1;
            } else if (move == 'R') {
                distance_1 += 1;
                distance_2 += 1;
            } else if (move == '_') {
                distance_1 += 1;
                distance_2 -= 1;
            }
        }
        return Math.Max(Math.Abs(distance_1), Math.Abs(distance_2));
    }
}
