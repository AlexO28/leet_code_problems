/*
There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer. A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing to the character 'a'.
Each second, you may perform one of the following operations:
Move the pointer one character counterclockwise or clockwise.
Type the character the pointer is currently on.
Given a string word, return the minimum number of seconds to type out the characters in word.
*/
using System;


public class Solution {
    public int MinTimeToType(string word) {
        int numberOfSeconds = 0;
        char pointer = 'a';
        foreach (char letter in word) {
            if (pointer == letter) {
                ++numberOfSeconds;
            } else {
                int difference = Math.Abs(letter - pointer);
                difference = Math.Min(difference, 26 - difference);
                pointer = letter;
                numberOfSeconds += difference + 1;
            }
        }
        return numberOfSeconds;
    }
}
