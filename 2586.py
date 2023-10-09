"""2586. Count the Number of Vowel Strings in Range"""

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        
        # Create set of vowels to allow constant time lookup
        vowels = set("AEIOUaeiou") 
        
        # Initialize count
        count = 0

        # Loop through elements in array within range
        for i in range(left, right + 1):
            # Check if first and last elements are vowels
            if words[i][0] in vowels and words[i][-1] in vowels:
                count += 1
        
        return count
