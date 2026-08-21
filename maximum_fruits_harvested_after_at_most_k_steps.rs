/*
Fruits are available at some positions on an infinite x-axis. You are given a 2D integer array fruits where fruits[i] = [positioni, amounti] depicts amounti fruits at the position positioni. fruits is already sorted by positioni in ascending order, and each positioni is unique.
You are also given an integer startPos and an integer k. Initially, you are at the position startPos. From any position, you can either walk to the left or right. It takes one step to move one unit on the x-axis, and you can walk at most k steps in total. For every position you reach, you harvest all the fruits at that position, and the fruits will disappear from that position.
Return the maximum total number of fruits you can harvest.
*/
impl Solution {
    pub fn max_total_fruits(fruits: Vec<Vec<i32>>, start_pos: i32, k: i32) -> i32 {
        let mut ans = 0;
        let mut i = 0;
        let mut s = 0;
        for j in 0..fruits.len() {
            s += fruits[j][1];
            while (i <= j) && (fruits[j][0] - fruits[i][0] + (start_pos - fruits[i][0]).abs().min((start_pos - fruits[j][0]).abs()) > k) {
                s -= fruits[i][1];
                i += 1;
            }
            ans = ans.max(s);
        }
        return ans;
    }
}
