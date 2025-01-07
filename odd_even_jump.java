/* You are given an integer array arr. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.
You may jump forward from index i to index j (with i < j) in the following way:
#During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that arr[i] >= arr[j] and arr[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
It may be the case that for some index i, there are no legal jumps.
A starting index is good if, starting from that index, you can reach the end of the array (index arr.length - 1) by jumping some number of times (possibly 0 or more than once).
Return the number of good starting indices. */
class Solution {
    private Integer[][] dp;
    private int[][] nextIndices;

    public int oddEvenJumps(int[] arr) {
        TreeMap<Integer, Integer> valueToIndexMap = new TreeMap<>();
        dp = new Integer[arr.length][2];
        nextIndices = new int[arr.length][2];      
        for (int i = arr.length - 1; i >= 0; --i) {
            Map.Entry<Integer, Integer> higher = valueToIndexMap.ceilingEntry(arr[i]);
            nextIndices[i][1] = higher == null ? -1 : higher.getValue();          
            Map.Entry<Integer, Integer> lower = valueToIndexMap.floorEntry(arr[i]);
            nextIndices[i][0] = lower == null ? -1 : lower.getValue();          
            valueToIndexMap.put(arr[i], i);
        }
      
        int goodStartingIndicesCount = 0;
        for (int i = 0; i < arr.length; ++i) {
            goodStartingIndicesCount += performJump(i, 1, arr.length);
        }
        return goodStartingIndicesCount;
    }

    private int performJump(int index, int jumpType, int arrayLength) {
        if (index == arrayLength - 1) {
            return 1;
        }
        if (nextIndices[index][jumpType] == -1) {
            return 0;
        }
        if (dp[index][jumpType] != null) {
            return dp[index][jumpType];
        }
        return dp[index][jumpType] = performJump(nextIndices[index][jumpType], jumpType ^ 1, arrayLength);
    }
}
