class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        d = {}
        for num in nums:
            key = num

            if key not in d:
                d[key] = []
            d[key].append(num)

        found = False
        for key in d:
            if len(d[key]) > 1:
                found = True
                break

        if found: 
            return True
        else: 
            return False

# We'll use a simple hashset for this. Duplicates quite literally mean if there are more than one value in a key since every unique element
# has a new key. Therefore, we'll iterate through nums and initialise them as a key. If key is not found in d, then we'll initialise a new
# set of values for that key. Otherwise, we'll just append it for that key.
# Then, we'll have a flag and go through keys in d. If the length of a key is greater than 1, it means it has two values which are quite
# literally duplicates.