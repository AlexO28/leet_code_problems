# You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book. You are also given an integer shelfWidth.
# We want to place these books in order onto bookcase shelves that have a total width shelfWidth.
# We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.
# Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.
# For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
# Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.
from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        if len(books) == 1:
            return books[0][1]
        min_height = [0] * (len(books) + 1)
        for i in range(1, len(books) + 1):
            height = books[i - 1][1]
            min_height[i] = min_height[i - 1] + height
            total_width = books[i - 1][0]
            for j in range(i - 1, 0, -1):
                total_width += books[j - 1][0]
                if total_width > shelfWidth:
                    break
                height = max(books[j - 1][1], height)
                min_height[i] = min(min_height[i], min_height[j - 1] + height)
        return min_height[-1]
