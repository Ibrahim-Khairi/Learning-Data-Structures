class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        window_dict = {}
        left = right = 0

        for right in range(len(s)):
            window_dict[s[right]] = window_dict.get(s[right], 0) + 1
            max_count = max(window_dict.values())
            if right-left+1-max_count > k:
                window_dict[s[left]] -= 1
                if window_dict[s[left]] == 0:
                    window_dict.pop(s[left])
                left += 1

        return right-left+1

# We just need to check the longest window with the most repeated counts of a character and only k amounts of any other character.
# We'll apply the same thing we did in maximise_the_confusion_of_an_exam.py.
# Keep adding s[right] to the window_dict, and get the most repeated character's count through max(window_dict.values()). We can then
# check that against the length of the window and see if that's bigger than k. If it is, then we need to shrink the window from the
# left.
# At the end, we can just return the length of the window.