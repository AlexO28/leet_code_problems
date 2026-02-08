# Write a solution to analyze AI prompt usage patterns based on the following requirements:
# For each user, calculate the total number of prompts they have submitted.
# For each user, calculate the average tokens used per prompt (Rounded to 2 decimal places).
# Only include users who have submitted at least 3 prompts.
# Only include users who have submitted at least one prompt with tokens greater than their own average token usage.
# Return the result table ordered by average tokens in descending order, and then by user_id in ascending order.
import pandas as pd


def find_users_with_high_tokens(prompts: pd.DataFrame) -> pd.DataFrame:
    prompts["tokens_2"] = prompts["tokens"]
    prompts = (
        prompts.groupby("user_id")
        .agg({"prompt": "count", "tokens": "mean", "tokens_2": "max"})
        .reset_index()
        .rename(columns={"prompt": "prompt_count", "tokens": "avg_tokens"})
    )
    prompts["avg_tokens"] = prompts["avg_tokens"].apply(lambda x: round(x, 2))
    prompts = prompts.loc[
        (prompts["prompt_count"] >= 3) & (prompts["tokens_2"] > prompts["avg_tokens"])
    ]
    del prompts["tokens_2"]
    return prompts.sort_values(by=["avg_tokens", "user_id"], ascending=[False, True])

