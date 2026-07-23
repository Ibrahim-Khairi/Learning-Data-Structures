class Solution(object):
    def findLHS(self, nums):
        """
        :type s: str
        :rtype: str
        """

        freq_map = {}
        for x in range(len(nums)):
            freq_map[nums[x]] = freq_map.get(nums[x], 0) + 1

        harmonious_sequence = 0
        for right in range(len(nums)):
            if nums[right] in freq_map and nums[right]+1 in freq_map:
                harmonious_sequence = max(harmonious_sequence, freq_map[nums[right]] + freq_map[nums[right]+1])

        return harmonious_sequence

# Initially, we draw up the frequency map for each digit in the array.
# We can initialize a harmonious_sequence to be returned.
# We can then iterate through the entire nums array again and check if nums[right] and nums[right]+1 exists in the freq_map. If it does, that
# means that is a harmonious_sequence. We can then just simply take the max of our current harmonious_sequence and the current 2 integer
# frequencies added up.