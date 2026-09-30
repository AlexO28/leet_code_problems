# You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.
# The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.
# Return the minimum unfairness of all distributions.
from math import inf


class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        self.ans = inf
        self.count = [0] * k
        self.cookies = cookies
        self.k = k
        self.cookies.sort(reverse=True)
        self.search(0)
        return self.ans

    def search(self, i):
        if i >= len(self.cookies):
            self.ans = max(self.count)
        else:
            for j in range(self.k):
                if (self.count[j] + self.cookies[i] < self.ans) and (
                    j == 0 or self.count[j] != self.count[j - 1]
                ):
                    self.count[j] += self.cookies[i]
                    self.search(i + 1)
                    self.count[j] -= self.cookies[i]
