# A social media company is trying to monitor activity on their site by analyzing the number of tweets that occur in select periods of time. These periods can be partitioned into smaller time chunks based on a certain frequency (every minute, hour, or day).
# For example, the period [10, 10000] (in seconds) would be partitioned into the following time chunks with these frequencies:
# Every minute (60-second chunks): [10,69], [70,129], [130,189], ..., [9970,10000]
# Every hour (3600-second chunks): [10,3609], [3610,7209], [7210,10000]
# Every day (86400-second chunks): [10,10000]
# Notice that the last chunk may be shorter than the specified frequency's chunk size and will always end with the end time of the period (10000 in the above example).
# Design and implement an API to help the company with their analysis.
# Implement the TweetCounts class:
# TweetCounts() Initializes the TweetCounts object.
# void recordTweet(String tweetName, int time) Stores the tweetName at the recorded time (in seconds).
# List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) Returns a list of integers representing the number of tweets with tweetName in each time chunk for the given period of time [startTime, endTime] (in seconds) and frequency freq.
# freq is one of "minute", "hour", or "day" representing a frequency of every minute, hour, or day respectively.
import numpy as np
from typing import List


class TweetCounts:

    def __init__(self):
        self.tweets = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName in self.tweets:
            self.tweets[tweetName].append(time)
        else:
            self.tweets[tweetName] = [time]

    def getTweetCountsPerFrequency(
        self, freq: str, tweetName: str, startTime: int, endTime: int
    ) -> List[int]:
        if freq == "minute":
            frequency = 60
        elif freq == "hour":
            frequency = 3600
        else:
            frequency = 86400
        number_of_intervals = int(np.ceil((endTime - startTime + 1) / frequency))
        res = [0] * (number_of_intervals)
        for time in self.tweets[tweetName]:
            if (time >= startTime) and (time <= endTime):
                res[(time - startTime) // frequency] += 1
        return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
