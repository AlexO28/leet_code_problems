/*
In a garden represented as an infinite 2D grid, there is an apple tree planted at every integer coordinate. The apple tree planted at an integer coordinate (i, j) has |i| + |j| apples growing on it.
You will buy an axis-aligned square plot of land that is centered at (0, 0).
Given an integer neededApples, return the minimum perimeter of a plot such that at least neededApples apples are inside or on the perimeter of that plot.
*/
public class Solution {
    public long MinimumPerimeter(long neededApples) {
        long x = 1;
        while (2 * x * (x + 1) * (2 * x + 1) < neededApples) {
            ++x;
        }
        return 8 * x;
    }
}
