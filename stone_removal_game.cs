/*
Alice and Bob are playing a game where they take turns removing stones from a pile, with Alice going first.
Alice starts by removing exactly 10 stones on her first turn.
For each subsequent turn, each player removes exactly 1 fewer stone than the previous opponent.
The player who cannot make a move loses the game.
Given a positive integer n, return true if Alice wins the game and false otherwise.
*/
public class Solution {
    public bool CanAliceWin(int n) {
        bool alice = false;
        int etalon = 10;
        while (etalon > 0) {
            n -= etalon;
            if (n < 0) {
                return alice;
            } else {
                alice = !alice;
                --etalon;
            }
        }
        return alice;
    }
}
