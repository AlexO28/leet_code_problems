# Write a solution to find all books that are currently borrowed (not returned) and have zero copies available in the library.
# A book is considered currently borrowed if there exists a borrowing record with a NULL return_date
# Return the result table ordered by current borrowers in descending order, then by book title in ascending order.
import pandas as pd


def find_books_with_no_available_copies(
    library_books: pd.DataFrame, borrowing_records: pd.DataFrame
) -> pd.DataFrame:
    borrowing_records = (
        borrowing_records.loc[pd.isnull(borrowing_records["return_date"])][
            ["book_id", "borrower_name"]
        ]
        .drop_duplicates()
        .rename(columns={"borrower_name": "current_borrowers"})
    )
    tab = pd.merge(library_books, borrowing_records, how="inner", on="book_id")
    tab = (
        tab.groupby(
            ["book_id", "title", "author", "genre", "publication_year", "total_copies"]
        )["current_borrowers"]
        .count()
        .reset_index()
    )
    tab = tab.loc[tab["total_copies"] == tab["current_borrowers"]]
    return tab[
        ["book_id", "title", "author", "genre", "publication_year", "current_borrowers"]
    ].sort_values(by=["current_borrowers", "title"], ascending=[False, True])
