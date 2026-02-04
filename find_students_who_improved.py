# Write a solution to find the students who have shown improvement. A student is considered to have shown improvement if they meet both of these conditions:
# Have taken exams in the same subject on at least two different dates
# Their latest score in that subject is higher than their first score
# Return the result table ordered by student_id, subject in ascending order.
import pandas as pd


def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    scores_min = (
        scores.groupby(["student_id", "subject"])
        .agg({"exam_date": "min", "score": "first"})
        .reset_index()
    )
    scores_max = (
        scores.groupby(["student_id", "subject"])
        .agg({"exam_date": "max", "score": "last"})
        .reset_index()
    )
    scores = pd.merge(scores_min, scores_max, how="inner", on=["student_id", "subject"])
    scores = scores.loc[
        (scores["exam_date_x"] < scores["exam_date_y"])
        & (scores["score_x"] < scores["score_y"])
    ].rename(columns={"score_x": "first_score", "score_y": "latest_score"})
    return scores[["student_id", "subject", "first_score", "latest_score"]]
