/*
There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of n cities numbered from 0 to n - 1 and exactly n - 1 roads. The capital city is city 0. You are given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.
There is a meeting for the representatives of each city. The meeting is in the capital city.
There is a car in each city. You are given an integer seats that indicates the number of seats in each car.
A representative can use the car in their city to travel or change the car and ride with another representative. The cost of traveling between two cities is one liter of fuel.
Return the minimum number of liters of fuel to reach the capital city.
*/
function minimumFuelCost(roads: number[][], seats: number): number {
    const n = roads.length + 1;
    const g: number[][] = Array.from({ length: n }, () => []);
    for (const [a, b] of roads) {
        g[a].push(b);
        g[b].push(a);
    }
    let res: number = 0;
    const sz: number[] = Array(n).fill(1);
    const stk: number[][] = [[0, -1, 0]];
    while (stk.length) {
        const [a, fa, state] = stk.pop()!;
        if (state === 0) {
            stk.push([a, fa, 1]);
            for (const b of g[a]) {
                if (b !== fa) {
                    stk.push([b, a, 0]);
                }
            }
        } else {
            for (const b of g[a]) {
                if (b !== fa) {
                    const t: number = sz[b];
                    res += Math.ceil(t / seats);
                    sz[a] += t;
                }
            }
        }
    }
    return res;
};
