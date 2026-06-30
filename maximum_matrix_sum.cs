/*
You are given an n x n integer matrix. You can do the following operation any number of times:
Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.
Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.
*/
using System;


public class Solution {
    public long MaxMatrixSum(int[][] matrix) {
        int numberOfNegatives = 0;
        int smallestNumber = 1000000;
        long summa = 0;
        for (int i = 0; i < matrix.Length; ++i) {
            for (int j = 0; j < matrix[0].Length; ++j) {
                if (matrix[i][j] < 0) {
                    ++numberOfNegatives;
                }
                int absVal = Math.Abs(matrix[i][j]);
                smallestNumber = Math.Min(smallestNumber, absVal);
                summa += absVal;
            }
        }
        if ((smallestNumber == 0) || (numberOfNegatives % 2 == 0)) {
            return summa;
        } else {
            return summa - 2 * smallestNumber;
        }
    }
}
