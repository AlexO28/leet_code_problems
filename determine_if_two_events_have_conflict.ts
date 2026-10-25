/*
You are given two arrays of strings that represent two inclusive events that happened on the same day, event1 and event2, where:
event1 = [startTime1, endTime1] and
event2 = [startTime2, endTime2].
Event times are valid 24 hours format in the form of HH:MM.
A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).
Return true if there is a conflict between two events. Otherwise, return false.
*/
function haveConflict(event1: string[], event2: string[]): boolean {
    return Math.max(parseTime(event1[0]), parseTime(event2[0])) <= Math.min(parseTime(event1[1]), parseTime(event2[1]));
};

function parseTime(time: string): number {
    const [hour, minute] = time.split(":")
    return Number(hour) * 60 + Number(minute);
};
