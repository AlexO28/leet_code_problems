/*
You are given an integer n. There are n rooms numbered from 0 to n - 1.
You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.
Meetings are allocated to rooms in the following manner:
Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.
A half-closed interval [a, b) is the interval between a and b including a and not including b.
*/
//import { MinPriorityQueue, PriorityQueue } from '@datastructures-js/priority-queue';


function mostBooked(n: number, meetings: number[][]): number {
    meetings.sort((a, b) => a[0] - b[0]);
    const idle: MinPriorityQueue<number> = new MinPriorityQueue<number>();
    for (let i = 0; i < n; ++i) {
        idle.enqueue(i);
    }
    const busy: PriorityQueue<[number, number]> = new PriorityQueue<[number, number]>((a, b) => {
        if (a[0] === b[0]) {
            return a[1] - b[1];
        }
        return a[0] - b[0];
    });
    const cnt: number[] = new Array(n).fill(0);
    for (const v of meetings) {
        const s = v[0];
        const e = v[1];
        while (!busy.isEmpty() && busy.front()[0] <= s) {
            const i: number = busy.dequeue()[1];
            idle.enqueue(i);
        }
        let i: number = 0;
        if (!idle.isEmpty()) {
            i = idle.dequeue();
            busy.enqueue([e, i]);
        } else {
            const x: [number, number] = busy.dequeue();
            i = x[1];
            busy.enqueue([x[0] + e - s, i]);
        }
        ++cnt[i];
    }
    let res: number = 0;
    for (let i = 0; i < n; ++i) {
        if (cnt[res] < cnt[i]) {
            res = i;
        }
    }
    return res;
};
