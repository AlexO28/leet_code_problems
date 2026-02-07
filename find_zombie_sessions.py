# Write a solution to identify zombie sessions, sessions where users appear active but show abnormal behavior patterns. A session is considered a zombie session if it meets ALL the following criteria:
# The session duration is more than 30 minutes.
# Has at least 5 scroll events.
# The click-to-scroll ratio is less than 0.20 .
# No purchases were made during the session.
# Return the result table ordered by scroll_count in descending order, then by session_id in ascending order.
# The result format is in the following example.
import pandas as pd
from datetime import datetime


def find_zombie_sessions(app_events: pd.DataFrame) -> pd.DataFrame:
    app_events["event_timestamp"] = app_events["event_timestamp"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S")) 
    sessions = app_events[["session_id", "user_id"]].drop_duplicates().reset_index(drop = True)
    sessions["session_duration_minutes"] = -1
    sessions["scroll_count"] = -1
    for j in range(len(sessions)):
        tab = app_events.loc[app_events["session_id"] == sessions.loc[j, "session_id"]]
        date_min = tab["event_timestamp"].min()
        date_max = tab["event_timestamp"].max()
        date_diff = (date_max - date_min).total_seconds() / 60
        if date_diff <= 30:
            continue
        number_of_scrolls = len(tab.loc[tab["event_type"] == "scroll"])
        if number_of_scrolls < 5:
            continue
        number_of_clicks = len(tab.loc[tab["event_type"] == "click"])
        if number_of_clicks / number_of_scrolls >= 0.2:
            continue
        if len(tab.loc[tab["event_type"] == "purchase"]) > 0:
            continue
        sessions.loc[j, "session_duration_minutes"] = date_diff
        sessions.loc[j, "scroll_count"] = number_of_scrolls
    sessions = sessions.loc[sessions["scroll_count"] > 0]
    return sessions.sort_values(by = ["scroll_count", "session_id"], ascending = [False, True])
