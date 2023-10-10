"""2496. Maximum Value of String in an Array"""

def maximumValue(self, strs: List[str]) -> int:

    mx = 0 # Initialize max value as zero

    # Loop through each string
    for string in strs:
        if string.isdigit():
            # Set value to int if only digits
            value = int(string)
        else:
            # Otherwise string's value is its length
            value = len(string)
        mx = max(value, mx) # Check if value is greater than previous mxa
    
    return mx

