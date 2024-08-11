# There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.
# A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:
# age[y] <= 0.5 * age[x] + 7
# age[y] > age[x]
# age[y] > 100 && age[x] < 100
# Otherwise, x will send a friend request to y.
# Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.
# Return the total number of friend requests made.
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        if len(ages) == 1:
            return 0
        number_of_requests = 0
        ages_freqs = {}
        for age in ages:
            if age in ages_freqs:
                ages_freqs[age] += 1
            else:
                ages_freqs[age] = 1
        for age1 in ages_freqs.keys():
            for age2 in ages_freqs.keys():
                if self.friendRequest(age1, age2):
                    if age1 == age2:
                        number_of_requests += (ages_freqs[age1] - 1)*ages_freqs[age1]
                    else:
                        number_of_requests += ages_freqs[age1]*ages_freqs[age2]
        return number_of_requests

    def friendRequest(self, age1, age2):
        return not ((age2 <= 0.5 * age1 + 7) or (age2 > age1) or ((age2 > 100) and (age1 < 100)))
