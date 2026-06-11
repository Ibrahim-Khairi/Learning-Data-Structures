class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        character_array = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        number_array = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        left = 0
        right = len(s) - 1
        palindrome = True
        while left < right:
            while left < right and not (s[left].upper() in character_array or s[left] in number_array):
                left += 1
            while left < right and not (s[right].upper() in character_array or s[right] in number_array):
                right -= 1

            if s[left].lower() != s[right].lower():
                palindrome = False

            left += 1
            right -= 1

        return palindrome

# First, we need a way to deal with non-alphanumeric characters. Therefore, we can just simply declare character and number arrays that
# include all the alphabets and numbers, to compare with them. If they are not part of these arrays then they are either spaces or special
# symbols.
# Now we need a way to run comparisons between the left most and the right most.
# Since we need to move inwards, these pointers will have to be incremented and decremented, respectively.
# So the left pointer will be incremented by 1, the right pointer will be decremented by 1.
# We keep on incrementing/decrementing them until the pointers CROSS. Not equalise, rather cross.
# So, while left < right, we keep on changing the pointers.
# In this while loop, we further need two loops that keep on skipping non-alphanumeric characters. To skip, we further need to increment
# or decrement the pointers, therefore, we need the left < right condition again.
# Then in each of these while loops we see whether the character can be found in the arrays we initialised or not, and we deal with the
# specific pointers.
# Finally, we compare whether the character at the left is equal to the character at the right. Since we need to ignore case-sensitivity, we
# can just change them to either lowercase or uppercase.