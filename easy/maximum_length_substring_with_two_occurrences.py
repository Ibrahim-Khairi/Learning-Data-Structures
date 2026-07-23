class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left = 0
        max_length = 0
        freq_map = {}

        for right in range(len(s)):
            if s[right] in freq_map:
                freq_map[s[right]] += 1
            else:
                freq_map[s[right]] = 1

            while freq_map[s[right]] > 2:
                freq_map[s[left]] -= 1
                left += 1

            max_length = max(max_length, right-left+1)

        return max_length

# So initially, we declare a left pointer, max_length and a frequency map freq_map.
# The max_length is to keep a counter of the longest substring that we have to return with at most two occurrences of each character.
# The freq_map helps keep track of the frequencies of said characters.
# We loop the right pointer through the entire string, appending it into the frequency_map if it doesn't exist, or just adding to its frequency.
# Then, we check whether the frequency of that character has exceeded 2. If it does, then we need to increment left, and get it out of our
# frequency map by decrementing the frequency of the character at which left is pointer.
# Once we're done with all checks, we just make the max_length the bigger of its current-self, or right-left+1 which is basically the size of our
# window.