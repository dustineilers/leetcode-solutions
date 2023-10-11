"""2269. Find the K-Beauty of a Number"""

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        count = 0

        # Loop through all possible substrings
        for i in range(len(str(num)) - k + 1):

            # Check if substring meets criteria
            if (digit := int(str(num)[i:i+k])) != 0 and num % digit == 0:
                count += 1

        return count