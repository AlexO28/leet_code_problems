/*
You are given a positive integer n. Each digit of n has a sign according to the following rules:
The most significant digit is assigned a positive sign.
Each other digit has an opposite sign to its adjacent digits.
Return the sum of all digits with their corresponding sign.
*/
public class Solution {
    public int AlternateDigitSum(int n) {
        string numStr = n.ToString();
        int summa = 0;
        for (int j = 0; j < numStr.Length; ++j) {
            if (j % 2 == 0) {
                summa += numStr[j] - '0';
            } else {
                summa -= numStr[j] - '0';
            }
        }
        return summa;
    }
}
