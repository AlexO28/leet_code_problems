/*
Given two positive integers a and b, return the number of common factors of a and b.
An integer x is a common factor of a and b if x divides both a and b.
*/
function commonFactors(a: number, b: number): number {
    let res: number = 0;
    for (let i: number = 1; i <= Math.min(a, b); ++i) {
        if ((a % i == 0) && (b % i == 0)) {
            ++res;
        }
    }
    return res;
};
