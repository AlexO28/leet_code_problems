/*
An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".
For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.
*/
function longestContinuousSubstring(s: string): number {
    let start: string = "a";
    let res: number = 0;
    while (start <= "z") {
        let candidate: string = start;
        while (true) {
            if (!s.includes(candidate)) {
                break;
            } else {
                res = Math.max(res, candidate.length);
                let next: string = shift(candidate);
                if (next > "z") {
                    break;
                } else {
                    candidate += next;
                }
            }
        }
        start = shift(start);
    }
    return res;
};

function shift(x: string) {
    return String.fromCharCode(x.charCodeAt(x.length - 1) + 1);
}
