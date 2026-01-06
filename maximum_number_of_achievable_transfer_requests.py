# We have n buildings numbered from 0 to n - 1. Each building has a number of employees. It's transfer season, and some employees want to change the building they reside in.
# You are given an array requests where requests[i] = [fromi, toi] represents an employee's request to transfer from building fromi to building toi.
# All buildings are full, so a list of requests is achievable only if for each building, the net change in employee transfers is zero. This means the number of employees leaving is equal to the number of employees moving in. For example if n = 3 and two employees are leaving building 0, one is leaving building 1, and one is leaving building 2, there should be two employees moving to building 0, one employee moving to building 1, and one employee moving to building 2.
# Return the maximum number of achievable requests.
from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.n = n
        self.requests = requests
        ans = 0
        for mask in range(1 << len(self.requests)):
            cnt = mask.bit_count()
            if ans < cnt and self.check(mask):
                ans = cnt
        return ans

    def check(self, mask):
        cnt = [0] * self.n
        for i, (f, t) in enumerate(self.requests):
            if mask >> i & 1:
                cnt[f] -= 1
                cnt[t] += 1
        for v in cnt:
            if v != 0:
                return False
        return True
