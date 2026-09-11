/*
You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.
Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.
*/
import java.util.HashSet;
import java.util.Set;


class Solution {
    public int totalNumbers(int[] digits) {
        Set<Integer> numbers = new HashSet<>();
        for (int i = 0; i < digits.length; ++i) {
            for (int j = 0; j < digits.length; ++j) {
                if ((i != j) && (digits[i] != 0)) {
                    for (int k = 0; k < digits.length; ++k) {
                        if ((i != k) && (j != k) && (digits[k] % 2 == 0)) {
                            numbers.add(100 * digits[i] + 10 * digits[j] + digits[k]);
                        }
                    }
                }
            }
        }
        System.out.println(numbers);
        return numbers.size();
    }
}
