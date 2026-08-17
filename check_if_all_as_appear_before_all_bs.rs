/*
Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.
*/
impl Solution {
    pub fn check_string(s: String) -> bool {
        let mut saw_a = false;
        let mut saw_b = false;
        for elem in s.chars() {
            if (elem == 'a') {
                if (saw_b) {
                    return false;
                } else {
                    saw_a = true;
                }
            } else {
                saw_b = true;
            }
        }
        true
    }
}
