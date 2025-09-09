# On day 1, one person discovers a secret.
# You are given an integer delay, which means that each person will share the secret with a new person every day, starting from delay days after discovering the secret. You are also given an integer forget, which means that each person will forget the secret forget days after discovering it. A person cannot share the secret on the same day they forgot it, or on any day afterwards.
# Given an integer n, return the number of people who know the secret at the end of day n. Since the answer may be very large, return it modulo 109 + 7
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        buffer_size = (n << 1) + 10
        people_knowing_secret = [0] * buffer_size
        new_people_each_day = [0] * buffer_size
        new_people_each_day[1] = 1
        for day in range(1, n + 1):
            if new_people_each_day[day] > 0:
                people_knowing_secret[day] += new_people_each_day[day]
                people_knowing_secret[day + forget] -= new_people_each_day[day]
                start_sharing_day = day + delay
                stop_sharing_day = day + forget
                for sharing_day in range(start_sharing_day, stop_sharing_day):
                    new_people_each_day[sharing_day] += new_people_each_day[day]
        return sum(people_knowing_secret[: n + 1]) % (10**9 + 7)
