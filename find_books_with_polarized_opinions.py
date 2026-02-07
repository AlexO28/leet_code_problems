# Write a solution to find books that have polarized opinions - books that receive both very high ratings and very low ratings from different readers.
# A book has polarized opinions if it has at least one rating ≥ 4 and at least one rating ≤ 2
# Only consider books that have at least 5 reading sessions
# Calculate the rating spread as (highest_rating - lowest_rating)
# Calculate the polarization score as the number of extreme ratings (ratings ≤ 2 or ≥ 4) divided by total sessions
# Only include books where polarization score ≥ 0.6 (at least 60% extreme ratings)
# Return the result table ordered by polarization score in descending order, then by title in descending order.
# The polarization score should be rounded to 2 decimal places.
import pandas as pd


def find_polarized_books(
    books: pd.DataFrame, reading_sessions: pd.DataFrame
) -> pd.DataFrame:
    books["rating_spread"] = -1
    books["polarization_score"] = -1
    for j in range(len(books)):
        tab = reading_sessions.loc[
            reading_sessions["book_id"] == books.loc[j, "book_id"]
        ]
        if len(tab) < 5:
            continue
        num_good = len(tab.loc[tab["session_rating"] >= 4])
        num_bad = len(tab.loc[tab["session_rating"] <= 2])
        if (num_good > 0) and (num_bad > 0):
            polarization_score = round((num_bad + num_good) / len(tab) + 0.0001, 2)
            if polarization_score < 0.6:
                continue
            spread = tab["session_rating"].max() - tab["session_rating"].min()
            books.loc[j, "rating_spread"] = spread
            books.loc[j, "polarization_score"] = polarization_score
    books = books.loc[books["polarization_score"] >= 0]
    return books.sort_values(by=["polarization_score", "title"], ascending=False)
