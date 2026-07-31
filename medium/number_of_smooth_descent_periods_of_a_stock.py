class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        descent_periods = 0
        consecutive_descents = 1

        for right in range(len(prices)):
            if right > 0 and prices[right] == prices[right-1]-1:
                consecutive_descents += 1
            else:
                consecutive_descents = 1
            descent_periods += consecutive_descents

        return descent_periods

# So, in this, we basically just need a streak counter, in order to see how many consecutive sequences of descension we have in the prices.
# Therefore, we declare a descent_periods counter that'll actually be returned. We also declare a consecutive_descents counter will either
# increment if an element is exactly 1 less than it's previous element, or stay 1. Every single element in the array itself is counted as a descent
# period, therefore we're initiating this as 1 since this is what we are going to be incrementing our descent_periods counter with.
# So, we just check if right > 0 (because we need to subtract it from the previous element), and then check if right is the same as it's previous
# element-1. If yes, then we increment the consecutive_descents, or it remains 1.
# Finally, we increment the descent_periods with that streak.