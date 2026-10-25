/*
There are n employees, each with a unique id from 0 to n - 1.
You are given a 2D integer array logs where logs[i] = [idi, leaveTimei] where:
idi is the id of the employee that worked on the ith task, and
leaveTimei is the time at which the employee finished the ith task. All the values leaveTimei are unique.
Note that the ith task starts the moment right after the (i - 1)th task ends, and the 0th task starts at time 0.
Return the id of the employee that worked the task with the longest time. If there is a tie between two or more employees, return the smallest id among them.
*/
function hardestWorker(n: number, logs: number[][]): number {
    const info: Map<number, number> = new Map<number, number>();
    let last: number = 0;
    let maxTime: number = 0;
    for (let i: number = 0; i < logs.length; ++i) {
        let duration: number = logs[i][1] - last;
        if (info.has(logs[i][0])) {
            info.set(logs[i][0], Math.max(info.get(logs[i][0]), duration));
        } else {
            info.set(logs[i][0], duration);
        }
        maxTime = Math.max(maxTime, info.get(logs[i][0]));
        last = logs[i][1];
    }
    const ids: number[] = [];
    for (const [key, value] of info) {
        if (value == maxTime) {
            ids.push(key);
        }
    }
    return Math.min(...ids);
};
