/*You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.
Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.
An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.*/
public class Solution {
    public bool IsCovered(int[][] ranges, int left, int right) {
        for (int num = left; num <= right; num += 1) {
            bool found = false;
            foreach (int[] range in ranges) {
                if ((num >= range[0]) && (num <= range[1])) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                return false;
            }
        }
        return true;
    }
}
