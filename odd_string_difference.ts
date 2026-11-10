/*
You are given an array of equal-length strings words. Assume that the length of each string is n.
Each string words[i] can be converted into a difference integer array difference[i] of length n - 1 where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference between two letters is the difference between their positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.
All the strings in words have the same difference integer array, except one. You should find that string.
Return the string in words that has different difference integer array.
*/
function oddString(words: string[]): string {
    const differences: bigint[] = new Array(words.length).fill(0);
    for (let j: number = 0; j < words.length; ++j) {
        let num: bigint = 0n;
        let multiplier: bigint = 1n;
        for (let i: number = 1; i < words[j].length; ++i) {
            num += BigInt((words[j].charCodeAt(i) - words[j].charCodeAt(i - 1))) *  multiplier;
            multiplier *= BigInt(10);
        }
        differences[j] = num;
    }
    if (differences[0] == differences[1]) {
        for (let i: number = 1; i < differences.length; ++i) {
            if (differences[i] != differences[0]) {
                return words[i];
            }
        }
    } else if (differences[0] == differences[2]) {
        return words[1];
    } else {
        return words[0];
    }
};
