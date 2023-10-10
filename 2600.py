"""2600. K Items With the Maximum Sum"""

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        sol = 0

        # First pick ones
        while numOnes > 0 and k > 0:
            sol += 1
            numOnes -= 1
            k -= 1

        # Then pick zeros
        while numZeros > 0 and k > 0:
            numZeros -= 1
            k -= 1
        
        # Then pick negative ones
        while numNegOnes > 0 and k > 0:
            sol -= 1
            numNegOnes -= 1
            k -= 1

        return sol