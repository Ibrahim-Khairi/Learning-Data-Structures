class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            profit = prices[i] - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit

# First solution:
'''        
    if len(prices) > 1:
        min = prices[0]
        for i in range(1, len(prices) - 1):
            if prices[i] < min:
                min = prices[i]

        max = prices[prices.index(min) + 1]
        for i in range(prices.index(min), len(prices)):
            if prices[i] > max:
                max = prices[i]

        profit = 0
        if max > min:
            profit = max - min
        else:
            profit = 0
    else:
        profit = 0

    return profit
'''
# So at first I thought lowest price is the best time to buy and the highest price is the best time to sell. We'll only be checking the
# highest element after we have bought a stock. Therefore, we can derive the profit if we just subtract these two prices.
# However, it failed on scenarios where it wasn't always about highest - lowest prices.
# If an array is [3,2,6,5,0,3], my solution would've given 3 (3-0), however it should've been 4 (6-2).

# Second Solution:
'''
    max_profit = 0
    for x in range(0, len(prices)):
        for y in range(x+1, len(prices)):
            profit = prices[y] - prices[x]
            if profit > max_profit:
                max_profit = profit

    return max_profit
'''
# Then we tried this second solution. This solution takes every current price and compares it with every other price deriving profit at each
# iteration. If it exceeds then our previous max_profit, it overwrites it. However, the problem with this was, it had nested for loops.
# O(n^2) solution took too long on a LeetCode test case where they gave us literal 10,000 prices/elements.
# Therefore, we tried to find an O(n) solution.

# Third Solution:
# The one we implemented.
# In this, we'll just need to track the lowest price. Then for each price, we'll calculate the profit. If it exceeds the previous max_profit,
# then we'll simply overwrite the max profit.

# Looked easy at the first sight I can't lie. I stand corrected sure as heck.