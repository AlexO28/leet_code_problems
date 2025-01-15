# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Implement the TimeMap class:
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
import bisect


class TimeMap:

    def __init__(self):
        self.keys_data_1 = {}
        self.keys_data_2 = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keys_data_1:
            self.keys_data_1[key].append(timestamp)
            self.keys_data_2[key].append(value)
        else:
            self.keys_data_1[key] = [timestamp]
            self.keys_data_2[key] = [value]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.keys_data_1:
            ind = bisect.bisect(self.keys_data_1[key], timestamp)
            if ind == 0:
                return ""
            return self.keys_data_2[key][ind-1]
        else:
            return ""
