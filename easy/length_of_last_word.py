class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_pointer = len(s) - 1
        char_count = 0

        while char_pointer > 0:
            if s[char_pointer] != " ":
                while s[char_pointer] != " " and char_pointer >= 0:
                    char_pointer -= 1
                    char_count += 1
                break
            else:
                char_pointer -= 1

        return char_count

# First, I wrote this solution.
# char_pointer = len(s)-1
# char_count = 0
# while char_pointer > 0 and s[char_pointer] != " ":
#     char_count += 1
#     char_pointer -= 1
# It works fine, until you introduce spaces at the end of the string, then it simply returns 0 because no char was registered.
# So, we have to come up with a solution that ignores all the spaces and keeps moving char_pointer to the left, until we hit a non-space.
# The second we do, we just count characters till the space.
# The outer loop iterates till we hit 0, meaning empty string entirely.
# The condition checks whether we have spaces or not. If spaces are present, it just keeps going backwards. If there are no spaces, it means
# a character has been found. Therefore, now we just need to count the characters until the next space. So the same space condition can be
# used again.