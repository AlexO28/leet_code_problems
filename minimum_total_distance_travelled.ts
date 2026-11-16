/*
There are some robots and factories on the X-axis. You are given an integer array robot where robot[i] is the position of the ith robot. You are also given a 2D integer array factory where factory[j] = [positionj, limitj] indicates that positionj is the position of the jth factory and that the jth factory can repair at most limitj robots.
The positions of each robot are unique. The positions of each factory are also unique. Note that a robot can be in the same position as a factory initially.
All the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.
At any moment, you can set the initial direction of moving for some robot. Your target is to minimize the total distance traveled by all the robots.
Return the minimum total distance traveled by all the robots. The test cases are generated such that all the robots can be repaired.
Note that
All robots move at the same speed.
If two robots move in the same direction, they will never collide.
If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.
If a robot passes by a factory that reached its limits, it crosses it as if it does not exist.
If the robot moved from a position x to a position y, the distance it moved is |y - x|.
*/
function minimumTotalDistance(robot: number[], factory: number[][]): number {
    robot.sort((a, b) => a - b);
    factory.sort((a, b) => a[0] - b[0]);
    const f: number[][] = Array.from({ length: robot.length }, () => Array(factory.length).fill(-1));
    return search(0, 0, robot, factory, f);
};

function search(i: number, j: number, robot: number[], factory: number[][], f: number[][]): number {
    if (i === robot.length) {
        return 0;
    }
    if (j === factory.length) {
        return 1000000000000000;
    }
    if (f[i][j] !== -1) {
        return f[i][j];
    }
    let res: number = search(i, j + 1, robot, factory, f);
    let totalDist: number = 0;
    const [pos, capacity]: number[] = factory[j];
    for (let k: number = 0; k < capacity; ++k) {
        const temp: number = i + k;
        if (temp >= robot.length) {
            break;
        } else {
            totalDist += Math.abs(robot[temp] - pos);
            res = Math.min(res, totalDist + search(temp + 1, j + 1, robot, factory, f));
        }
    }
    return (f[i][j] = res);
};
