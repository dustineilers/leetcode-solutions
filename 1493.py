"""1493. Longest Subarray of 1's After Deleting One Element"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        i, j = 0, 0 # Left and right pointer of sliding window
        zeros = 0 # Count of zeros in subarray
        length = 0 # Maximum length

        while j < len(nums):
            # Check if right pointer encounters a zero
            if nums[j] == 0:
                zeros += 1

            # If more than one zero in window, increase left pointer until only one
            while zeros >= 2:
                if nums[i] == 0:
                    zeros -= 1
                i += 1

            # Check if new length is greater than max length
            length = max((j - i), length)

            j += 1 # Move right pointer
        
        return length