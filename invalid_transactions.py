# A transaction is possibly invalid if:
# the amount exceeds $1000, or;
# if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
# You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.
# Return a list of transactions that are possibly invalid. You may return the answer in any order.
from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        indices = []
        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(",")
            amount = int(amount)
            time = int(time)
            if amount > 1000:
                indices.append(i)
            if i < len(transactions) - 1:
                for j in range(i+1, len(transactions)):
                    name_alt, time_alt, amount_alt, city_alt = transactions[j].split(",")
                    time_alt = int(time_alt)
                    if (name == name_alt) and (city != city_alt) and abs(time - time_alt) <= 60:
                        indices.append(i)
                        indices.append(j)
        indices = list(set(indices))
        return [transactions[ind] for ind in indices]
