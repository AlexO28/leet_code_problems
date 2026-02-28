# You are given a string s and two integers x and y. You can perform two types of operations any number of times.
# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a = "a"
        b = "b"
        if x < y:
            x, y = y, x
            a, b = b, a
        ans = 0
        cnt1 = 0
        cnt2 = 0
        for c in s:
            if c == a:
                cnt1 += 1
            elif c == b:
                if cnt1 > 0:
                    ans += x
                    cnt1 -= 1
                else:
                    cnt2 += 1
            else:
                ans += min(cnt1, cnt2) * y
                cnt1 = 0
                cnt2 = 0
        ans += min(cnt1, cnt2) * y
        return ans
