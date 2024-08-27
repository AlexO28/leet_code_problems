# Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):
# When you get an instruction 'A', your car does the following:
# position += speed
# speed *= 2
# When you get an instruction 'R', your car does the following:
# If your speed is positive then speed = -1
# otherwise speed = 1
# Your position stays the same.
# For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.
# Given a target position target, return the length of the shortest sequence of instructions to get there.
class Solution:
    def racecar(self, target: int) -> int:
        dp = [0]*(target+1)
        for i in range(1, target+1):
            k = i.bit_length()
            power = 2 ** k
            if i == power - 1:
                dp[i] = k
            else:
                dp[i] = dp[power - i - 1] + k + 1
                power_j = 1
                for j in range(k - 1):
                    dp[i] = min(dp[i], dp[i - (power//2 - power_j)] + k - 1 + j + 2)
                    power_j *= 2
        return dp[-1]
