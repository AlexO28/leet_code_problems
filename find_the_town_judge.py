# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return n
        trust_dict = {}
        trusted_dict = {}
        for belief in trust:
            if belief[0] not in trust_dict:
                trust_dict[belief[0]] = 1
            if belief[1] in trusted_dict:
                trusted_dict[belief[1]] += 1
            else:
                trusted_dict[belief[1]] = 1
        if len(trust_dict.keys()) == n:
            return -1
        for j in range(1, n+1):
            if j not in trust_dict:
                if j in trusted_dict:
                    if trusted_dict[j] == n - 1:
                        return j
        return -1
