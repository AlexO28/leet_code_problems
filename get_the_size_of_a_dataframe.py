# Write a solution to calculate and display the number of rows and columns of players.
# Return the result as an array:
# [number of rows, number of columns]
# The result format is in the following example.
from typing import List
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [len(players), len(players.columns)]
