class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """

        count = 0

        for x in fruits:
            unplaced = 1
            for i in range(0, len(baskets)):
                if x <= baskets[i]:
                    baskets[i] = 0
                    unplaced = 0
                    break
            count += unplaced

        return count

# We'll declare a count as to how many fruit types are not placed yet.
# We'll run a for loop for each of the fruits, and initialize a variable "unplaced" as 1. This will change if we are able to place the fruit/
# We'll declare another inner for loop for the length of the baskets. If the current basket happens to be greater or equal to the fruit type
# that we are iterating over, then we can just place the fruit in that basket. To do that, we'll declare at 0, and change unplaced to 0, and
# break that for loop because we can move onto the next fruit type now. The reason why we change that basket to 0 is because fruits can only
# be placed in a basket with a capacity greater than or equal to the guantity of that fruit type. Therefore, if we change the basket's
# capacity to 0, automatically, no fruit type will be placed in it further. Also, since that fruit type has already been placed, we can change
# the unplaced variable to 0. After we get out of the basket-checking loop, we can just increment it to the count of the fruits that have not
# been placed. If a fruit type has been placed, the count will not be incremented (since unplaced is 0).