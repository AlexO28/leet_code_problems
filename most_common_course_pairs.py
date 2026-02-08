# Write a solution to identify skill mastery pathways by analyzing course completion sequences among top-performing students:
# Consider only top-performing students (those who completed at least 5 courses with an average rating of 4 or higher).
# For each top performer, identify the sequence of courses they completed in chronological order.
# Find all consecutive course pairs (Course A → Course B) taken by these students.
# Return the pair frequency, identifying which course transitions are most common among high achievers.
# Return the result table ordered by pair frequency in descending order and then by first course name and second course name in ascending order.
import pandas as pd


def topLearnerCourseTransitions(course_completions: pd.DataFrame) -> pd.DataFrame:
    students = (
        course_completions.groupby("user_id")
        .agg({"course_id": "count", "course_rating": "mean"})
        .reset_index()
    )
    students = students.loc[
        (students["course_id"] >= 5) & (students["course_rating"] >= 4)
    ][["user_id"]].reset_index(drop=True)
    pairs = {}
    for j in range(len(students)):
        tab = (
            course_completions.loc[
                course_completions["user_id"] == students.loc[j, "user_id"]
            ]
            .sort_values(by="completion_date")
            .reset_index()
        )
        if len(tab) < 2:
            continue
        for j in range(1, len(tab)):
            pair = tab.loc[j - 1, "course_name"] + " --> " + tab.loc[j, "course_name"]
            if pair in pairs:
                pairs[pair] += 1
            else:
                pairs[pair] = 1
    first_courses = []
    second_courses = []
    transition_counts = []
    for pair in pairs:
        first, second = pair.split(" --> ")
        first_courses.append(first)
        second_courses.append(second)
        transition_counts.append(pairs[pair])
    return pd.DataFrame(
        {
            "first_course": first_courses,
            "second_course": second_courses,
            "transition_count": transition_counts,
        }
    ).sort_values(
        by=["transition_count", "first_course", "second_course"],
        ascending=[False, True, True],
        key=lambda col: col.str.lower() if col.dtype == "object" else col,
    )
