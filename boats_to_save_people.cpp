/*
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.
*/
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        if (people.size() == 1) return 1;
        int number_of_boats = 0;
        ranges::sort(people);
        for (int i = 0, j = people.size() - 1; i <= j; ++number_of_boats) {
            const int remainder = limit - people[j--];
            if (people[i] <= remainder) ++i;
        }
        return number_of_boats;
    }
};
