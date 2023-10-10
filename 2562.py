"""2562. Find the Array Concatenation Value"""

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        
        sol = 0 # Initialize solution
        
        while nums:
            if len(nums) >= 2:
                # Pop and concatenate first and last value
                sol += int(str(nums.pop(0)) + str(nums.pop())) 
            else:
                # Pop final value and add it to solution
                sol += nums.pop()
        return sol
