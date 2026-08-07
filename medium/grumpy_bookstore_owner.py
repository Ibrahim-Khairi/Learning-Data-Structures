class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """

        naturally_satisfied = 0
        for x in range(len(grumpy)):
            if not grumpy[x]:
                naturally_satisfied += customers[x]

        unsatisfied_customers = longest_unsatisfied = 0
        left = 0
        for right in range(len(customers)):
            if grumpy[right]:
                unsatisfied_customers += customers[right]
            if right-left+1 > minutes:
                if grumpy[left]:
                    unsatisfied_customers -= customers[left]
                left += 1
            longest_unsatisfied = max(unsatisfied_customers, longest_unsatisfied)

        return naturally_satisfied + longest_unsatisfied

# We first need to find the initial number of naturally satisfied customers. We can do this by iterating through the grumpy list
# and since the indices are consistent with the customers list, we can just check how many customers are being satisfied whenever
# the grumpy index is 0. We'll add that to the naturally_satisfied sum variable.
# We can then loop through the customers and have a fixed-size of k elements window slide through it. At each iteration we'll check if
# the owner is grumpy. If they are, then we'll just add it to the unsatisfied_customers sum variable.
# We'll then check if the length of the window has exceeded minutes. If it has, we'll just shrink it from the left.
# At the end of the iteration, we'll check whether the current window's unsatisfied customers are more than the previously
# longest_unsatisfied.
# After coming out of the loop, we can just add the two variables (naturally_satisfied and longest_unsatisfied) together to derive
# the final maximum number of customers that can be satisfied throughout the day after the owner utilises his technique.