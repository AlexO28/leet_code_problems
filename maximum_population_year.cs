/*
You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.
The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.
Return the earliest year with the maximum population.
*/
public class Solution {
    public int MaximumPopulation(int[][] logs) {
        const int startYear = 1950;
        int[] dataPerYear = new int[101];
        foreach (var entry in logs) {
            for (int j = entry[0]; j < entry[1]; ++j) {
                dataPerYear[j-startYear] += 1;
            }
        }
        int maxIndex = 0;
        for (int j = 0; j < dataPerYear.Length; ++j) {
            if (dataPerYear[j] > dataPerYear[maxIndex]) {
                maxIndex = j;
            }
        }
        return maxIndex + startYear;
    }
}
