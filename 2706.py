"""2706. Buy Two Chocolates"""

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort() # Sort the array of prices to find the lowest values
        return money - cost if (cost := prices[0] + prices[1]) <= money else money