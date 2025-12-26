# You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':
# if the ith character is 'Y', it means that customers come at the ith hour
# whereas 'N' indicates that no customers come at the ith hour.
# If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:
# For every hour when the shop is open and no customers come, the penalty increases by 1.
# For every hour when the shop is closed and customers come, the penalty increases by 1.
# Return the earliest hour at which the shop must be closed to incur a minimum penalty.
# Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        sum_Y = 0
        customers = list(customers)
        for customer in customers:
            if customer == "Y":
                sum_Y += 1
        sum_N = 0
        index = -1
        min_penalty = len(customers) + 1
        for j in range(len(customers)):
            penalty = sum_Y + sum_N
            if penalty < min_penalty:
                min_penalty = penalty
                index = j
            if customers[j] == "Y":
                sum_Y -= 1
            else:
                sum_N += 1
        penalty = sum_Y + sum_N
        if penalty < min_penalty:
            min_penalty = penalty
            index = len(customers)
        return index
