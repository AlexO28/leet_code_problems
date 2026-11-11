/*
A valid cut in a circle can be:
A cut that is represented by a straight line that touches two points on the edge of the circle and passes through its center, or
A cut that is represented by a straight line that touches one point on the edge of the circle and its center.
Some valid and invalid cuts are shown in the figures below.
Given the integer n, return the minimum number of cuts needed to divide a circle into n equal slices.
*/
function numberOfCuts(n: number): number {
    if (n == 1) {
        return 0;
    } else if (n % 2 == 0) {
        return Math.floor(n / 2);
    } else {
        return n;
    }
};
