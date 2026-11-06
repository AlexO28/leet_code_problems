/*
Given a positive integer n, there exists a 0-indexed array called powers, composed of the minimum number of powers of 2 that sum to n. The array is sorted in non-decreasing order, and there is only one way to form the array.
You are also given a 0-indexed 2D integer array queries, where queries[i] = [lefti, righti]. Each queries[i] represents a query where you have to find the product of all powers[j] with lefti <= j <= righti.
Return an array answers, equal in length to queries, where answers[i] is the answer to the ith query. Since the answer to the ith query may be too large, each answers[i] should be returned modulo 109 + 7.
*/
function productQueries(n: number, queries: number[][]): number[] {
    const powers: number[] = [];
    while (n > 0) {
        const x: number = n & -n;
        powers.push(x);
        n -= x;
    }
    const mod: number = 1000000007;
    const res: number[] = [];
    for (const [l, r] of queries) {
        let x: number = 1;
        for (let j: number = l; j <= r; ++j) {
            x = (x * powers[j]) % mod;
        }
        res.push(x);
    }
    return res;
};
