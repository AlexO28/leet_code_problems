# On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.
# You are given an integer n, an array languages, and an array friendships where:
# There are n languages numbered 1 through n,
# languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
# friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
# You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.
# Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.
from typing import List


class Solution:
    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]
    ) -> int:
        min_users = 501
        bad_friendships = []
        for u, v in friendships:
            languages_u = set(languages[u - 1])
            languages_v = set(languages[v - 1])
            if len(languages_u & languages_v) == 0:
                bad_friendships.append([u, v])
        for language in range(1, n + 1):
            users = []
            for u, v in bad_friendships:
                languages_u = set(languages[u - 1])
                languages_v = set(languages[v - 1])
                if language not in languages_u:
                    users.append(u)
                if language not in languages_v:
                    users.append(v)
            min_users = min(min_users, len(set(users)))
        return min_users
