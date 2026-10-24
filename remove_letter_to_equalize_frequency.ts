/*
You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.
Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.
Note:
The frequency of a letter x is the number of times it occurs in the string.
You must remove exactly one letter and cannot choose to do nothing.
*/
function equalFrequency(word: string): boolean {
    let info: number[] = Array(26).fill(0);
    const acode: number = "a".charCodeAt(0);
    for (const elem of word) {
        ++info[elem.charCodeAt(0) - acode];
    }
    for (let i: number = 0; i < info.length; ++i) {
        if (info[i] > 0) {
            --info[i];
            let maxFreq: number = Math.max(...info);
            let verdict: boolean = true;
            for (const num of info) {
                if ((num > 0) && (num != maxFreq)) {
                    verdict = false;
                    break;
                }
            }
            if (verdict) {
                return true;
            }
            ++info[i];
        }
    }
    return false;
};
