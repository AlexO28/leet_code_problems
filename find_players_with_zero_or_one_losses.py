# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.
# Return a list answer of size 2 where:
# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses_info = {}
        for match in matches:
            if match[0] not in losses_info:
                losses_info[match[0]] = 0
            if match[1] in losses_info:
                losses_info[match[1]] += 1
            else:
                losses_info[match[1]] = 1
        ans0 = []
        ans1 = []
        for player in losses_info:
            if losses_info[player] == 0:
                ans0.append(player)
            elif losses_info[player] == 1:
                ans1.append(player)
        ans0.sort()
        ans1.sort()
        return [ans0, ans1]
