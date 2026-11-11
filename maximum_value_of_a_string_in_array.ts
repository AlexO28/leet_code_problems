/*
The value of an alphanumeric string can be defined as:
The numeric representation of the string in base 10, if it comprises of digits only.
The length of the string, otherwise.
Given an array strs of alphanumeric strings, return the maximum value of any string in strs.
*/
function maximumValue(strs: string[]): number {
    let res: number = 0;
    for (const str of strs) {
        res = Math.max(res, calculateValue(str));
    }
    return res;
};

function calculateValue(str: string): number {
    if (/^\d+$/.test(str)) {
        return parseInt(str);
    } else {
        return str.length;
    }
};
