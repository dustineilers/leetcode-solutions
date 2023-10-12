"""1095. Find in Mountain Array"""

"""
It's not pretty, but it's my first Leetcode Hard!

Solution utlizes three binary searches. First, to find the peak.
Then, the left side is searched. If value is not in the left side, 
right side of the array is searched. 

To improve upon this solution, a function could be created and called
to perform the binary search.
"""

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        left = 0
        right = mountain_arr.length()

        while left < right:
            k = (left + right) // 2

            if (peak_left := mountain_arr.get(k - 1)) < (peak := mountain_arr.get(k)) and mountain_arr.get(k + 1) < peak:
                break
            elif peak_left < peak:
                left = k + 1          
            else:
                right = k

        if mountain_arr.get(k) == target:
            return k
        
        peak_index = k

        left = 0 
        right = peak_index

        while left < right:
            k = (left + right) // 2
            if (val := mountain_arr.get(k)) == target:
                return k
            elif (val := mountain_arr.get(k)) > target:
                right = k
            else:
                left = k + 1

        left = peak_index
        right = mountain_arr.length()

        while left < right:
            k = (left + right) // 2
            if (val := mountain_arr.get(k)) == target:
                return k
            elif val > target:
                left = k + 1
            else:
                right = k
                
        return -1