/*
Given a string s and an integer k, partition s into k substrings such that the letter changes needed to make each substring a semi-palindrome are minimized.
Return the minimum number of letter changes required.
A semi-palindrome is a special type of string that can be divided into palindromes based on a repeating pattern. To check if a string is a semi-palindrome:​
Choose a positive divisor d of the string's length. d can range from 1 up to, but not including, the string's length. For a string of length 1, it does not have a valid divisor as per this definition, since the only divisor is its length, which is not allowed.
For a given divisor d, divide the string into groups where each group contains characters from the string that follow a repeating pattern of length d. Specifically, the first group consists of characters at positions 1, 1 + d, 1 + 2d, and so on; the second group includes characters at positions 2, 2 + d, 2 + 2d, etc.
The string is considered a semi-palindrome if each of these groups forms a palindrome.
*/
function minimumChanges(s: string, k: number): number {
    const n: number = s.length + 1;
    const g: number[][] = Array.from({ length: n }, () => Array.from({ length: n }, () => Infinity));
    const f: number[][] = Array.from({ length: n }, () => Array.from({ length: k + 1 }, () => Infinity));
    f[0][0] = 0;
    for (let i: number = 1; i < n; ++i) {
        for (let j: number = 1; j < n; ++j) {
            const m: number = j - i + 1;
            for (let d: number = 1; d < m; ++d) {
                if (m % d === 0) {
                    let cnt: number = 0;
                    for (let l: number = 0; l < m; ++l) {
                        const r: number = (((m / d) | 0) - 1 - ((l / d) | 0)) * d + (l % d);
                        if (l >= r) {
                            break;
                        }
                        if (s[i - 1 + l] !== s[i - 1 + r]) {
                            ++cnt;
                        }
                    }
                    g[i][j] = Math.min(g[i][j], cnt);
                }
            }
        }
    }
    for (let i: number = 1; i < n; ++i) {
        for (let j: number = 1; j <= k; ++j) {
            for (let h: number = 0; h < i - 1; ++h) {
                f[i][j] = Math.min(f[i][j], f[h][j - 1] + g[h + 1][i]);
            }
        }
    }
    return f[s.length][k];
};
