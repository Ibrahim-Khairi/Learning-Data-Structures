class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """

        left = 0

        operations_required = 0
        for x in range(k):
            if blocks[x] == "W":
                operations_required += 1

        min_count = operations_required

        for right in range(k, len(blocks)):
            if blocks[left] == "W":
                operations_required -= 1
            if blocks[right] == "W":
                operations_required += 1
            left += 1
            if operations_required < min_count:
                min_count = operations_required

        return min_count

# Fixed-window problem.
# We'll initialize the first window as 0->k. Every white block that has to be changed would require one operation, therefore we can keep a
# counter operations_required and increment it upon every iteration of "W".
# At the end of this, we'll initialize a min_count as operations_required, this is the minimal number of operations currently.
# We'll then loop through k->len(blocks). Each left that leaves our window will decrement the operations_required if it's a white block, and
# each right that enters our window would increment the operations_required if it's a white block. At the end we can increment our left pointer,
# and check whether the current operations_required is less than min_count or not. If it is less than min_count, it'll become the new min_count.