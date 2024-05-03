/*There is a room with n bulbs labeled from 1 to n that all are turned on initially, and four buttons on the wall. Each of the four buttons has a different functionality where:
Button 1: Flips the status of all the bulbs.
Button 2: Flips the status of all the bulbs with even labels (i.e., 2, 4, ...).
Button 3: Flips the status of all the bulbs with odd labels (i.e., 1, 3, ...).
Button 4: Flips the status of all the bulbs with a label j = 3k + 1 where k = 0, 1, 2, ... (i.e., 1, 4, 7, 10, ...).
You must make exactly presses button presses in total. For each press, you may pick any of the four buttons to press.
Given the two integers n and presses, return the number of different possible statuses after performing all presses button presses.*/

#include <unordered_set>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int flipLights(int n, int presses) {
        n = min(n, 6);
        vector<int> operations = {0b111111, 0b010101, 0b101010, 0b100100};
        unordered_set<int> visitedConfigurations;
        for (int mask = 0; mask < 1 << 4; ++mask) {
            int count = __builtin_popcount(mask);
            if (count > presses || count % 2 != presses % 2) continue;
            int configuration = 0;
            for (int i = 0; i < 4; ++i) {
                if (mask >> i & 1) {
                    configuration ^= operations[i];
                }
            }
            configuration &= (1 << 6) - 1;
            configuration >>= (6 - n);
            visitedConfigurations.insert(configuration);
        }
        return visitedConfigurations.size();
    }
};
