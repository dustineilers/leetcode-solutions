"""2579. Count Total Number of Colored Cells"""

"""
There are two apparent approaches to solving 
this problem, using recursion or a mathematical equation.

The first solution uses recursion.
Recursion has O(n) time and space complexity.

The second approach uses math.
A mathematical equation has O(1) time and space complexity.

Clearly the second approach is much more efficient;
however, this problem is a good excercise in dynamic programming. 
"""

# Dynamic Programming Approach
class RecursionSolution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            # Number of cells added in each step plus the previous step
            return self.coloredCells(n - 1) + 4 * (n - 1)
        
# Mathematical Approach
class Solution:
    def coloredCells(self, n: int) -> int:
        # Mathematical equation for number of colored cells
        return 2 * n**2 - 2 * n + 1