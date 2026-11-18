/*
You are given a string s and a positive integer k.
Select a set of non-overlapping substrings from the string s that satisfy the following conditions:
The length of each substring is at least k.
Each substring is a palindrome.
Return the maximum number of substrings in an optimal selection.
A substring is a contiguous sequence of characters within a string.
*/
function maxPalindromes(s: string, k: number): number {
    const g: boolean[][] = Array.from({ length: s.length }, () => Array(s.length).fill(true));
    for (let i: number = s.length - 1; i >= 0; --i) {
        for (let j: number = i + 1; j < s.length; ++j) {
            g[i][j] = s[i] === s[j] && g[i + 1][j - 1];
        }
    }
    const f: number[] = Array(s.length + 1).fill(0);
    for (let i: number = s.length - 1; i >= 0; --i) {
        f[i] = f[i + 1];
        for (let j: number = i + k - 1; j < s.length; ++j) {
            if (g[i][j]) {
                f[i] = Math.max(f[i], 1 + f[j + 1]);
            }
        }
    }
    return f[0];
};
