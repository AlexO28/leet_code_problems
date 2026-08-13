# You are given a 0-indexed string hamsters where hamsters[i] is either:
# 'H' indicating that there is a hamster at index i, or
# '.' indicating that index i is empty.
# You will add some number of food buckets at the empty indices in order to feed the hamsters. A hamster can be fed if there is at least one food bucket to its left or to its right. More formally, a hamster at index i can be fed if you place a food bucket at index i - 1 and/or at index i + 1.
# Return the minimum number of food buckets you should place at empty indices to feed all the hamsters or -1 if it is impossible to feed all of them.
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        hamsters = list(hamsters)
        if len(hamsters) == 1:
            if hamsters[0] == "H":
                return -1
            else:
                return 0
        if (hamsters[0] == "H") and (hamsters[1] == "H"):
            return -1
        if len(hamsters) > 2:
            if (hamsters[-1] == "H") and (hamsters[-2] == "H"):
                return -1
        if len(hamsters) > 4:
            for i in range(1, len(hamsters) - 1):
                if (
                    (hamsters[i - 1] == "H")
                    and (hamsters[i] == "H")
                    and (hamsters[i + 1] == "H")
                ):
                    return -1
        num_baskets = 0
        for i in range(len(hamsters)):
            if hamsters[i] == "H":
                if hamsters[i - 1] == "*":
                    continue
                if i < len(hamsters) - 1:
                    if hamsters[i + 1] == ".":
                        hamsters[i + 1] = "*"
                        num_baskets += 1
                    else:
                        hamsters[i - 1] = "*"
                        num_baskets += 1
                else:
                    hamsters[i - 1] = "*"
                    num_baskets += 1
        return num_baskets
