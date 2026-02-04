# Write a solution to find the sum of amounts for odd and even transactions for each day. If there are no odd or even transactions for a specific date, display as 0.
# Return the result table ordered by transaction_date in ascending order.
import pandas as pd


def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions_odd = transactions.loc[transactions["amount"] % 2 == 1]
    transactions_even = transactions.loc[transactions["amount"] % 2 == 0]
    transactions_odd = (
        transactions_odd.groupby("transaction_date")["amount"].sum().reset_index()
    )
    transactions_even = (
        transactions_even.groupby("transaction_date")["amount"].sum().reset_index()
    )
    transactions = pd.merge(
        transactions_odd, transactions_even, how="outer", on="transaction_date"
    )
    transactions = transactions.rename(
        columns={"amount_x": "odd_sum", "amount_y": "even_sum"}
    )
    transactions["odd_sum"] = transactions["odd_sum"].fillna(0)
    transactions["even_sum"] = transactions["even_sum"].fillna(0)
    return transactions
