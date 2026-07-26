class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_dict = {"a":0, "b":0, "c":0}
        left = 0
        substring_count = 0

        for right in range(len(s)):
            char_dict[s[right]] += 1
            while char_dict["a"] > 0 and char_dict["b"] > 0 and char_dict["c"] > 0:
                char_dict[s[left]] -= 1
                left += 1
            substring_count += left

        return substring_count

# Since we know that we need abc in everything, and nothing else, we can just declare a dictionary with a b c as the keys, with 0 as values. We
# don't use a set here since we need to see the counts of each character/key, and that's not something that set() provides.
# We can then just declare a left pointer, and a substring_count counter variable to be returned.
# When we are looping our right pointer through the entire s string. At each iteration, we'll add 1 to that specific element's frequency.
# We then need a while loop to check that all 3 keys (a b c) are more than 0, and while that's true, we'll decrease the frequency of the key
# of the left pointer, and increment the left pointer.
# Since we know the window is now invalid, the character that was removed was char_dict[s[left-1]], and removing it broke the validity. So the
# last position where the window was still valid was left-1, therefore, we can just add till left in the substring_count counter.