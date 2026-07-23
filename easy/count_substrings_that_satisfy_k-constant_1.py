class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        freq_map = {}

        substrings_count = 0

        left = 0

        for right in range(0, len(s)):
            freq_map[s[right]] = freq_map.get(s[right], 0) + 1
            while freq_map.get("0", 0) > k and freq_map.get("1", 0) > k:
                freq_map[s[left]] -= 1
                left += 1
            substrings_count += right-left + 1

        return substrings_count

# We initialize the left pointer, freq_map, and substrings_count that is to be returned.
# Next, we loop right pointer through the entire string, drawing up a frequency map for each character.
# freq_map.get(s[right], 0) + 1 basically says, if it exists, then we just add +1 to it. Otherwise, we make it 0.
# then we want to see whether 0 and 1 are at most k. We'll get the frequency for 0s and 1s and we'll say while they are greater than k,
# we'll keep shrinking the window from the left. The second any one of them exceeds k, we can just increase a substring because that makes a
# valid binary string.