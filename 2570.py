"""2570. Merge Two 2D Arrays by Summing Values"""

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        values = {} # Initialize empty hashmaps

        # Loop through both arrays
        for x in (nums1 + nums2):
            # Sum if present
            if x[0] in values:
                values[x[0]] += x[1]
            # Otherwise create new entry
            else:
                values[x[0]] = x[1]

        # Sort keys to generate solution array
        keys = list(values.keys())
        sol = [[x, values[x]] for x in sorted(keys)]

        return sol