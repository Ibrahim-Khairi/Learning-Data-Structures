class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []

        for x in range(0, len(s)):
            if len(stack) == 0:
                stack.append(s[x])
            else:
                if (stack[len(stack) - 1].upper() == s[x] and stack[len(stack) - 1] == s[x].lower()) or (
                        stack[len(stack) - 1].lower() == s[x] and stack[len(stack) - 1] == s[x].upper()):
                    stack.pop()
                else:
                    stack.append(s[x])

        return_string = ""
        for char in stack:
            return_string += char

        return return_string

# Basically if any two characters happen ot be oppositely capitalised then they make the string bad.
# What we need to do is build a stack and push every character in it. If any character that we are about to push happens to be that same
# character but oppositely capitalised, then we pop the top character out.
# We can repeat this process until we are left with only good characters.
# Problem is, how to check if two letters are oppositely capitalised?
# char1 = "x"          |             char2 = "X"
# a) char1.upper() == char2 (True)
# b) char1.lower() == char2 (False)
# c) char2.upper() == char1 (False)
# d) char2.lower() == char1 (True)
# Therefore, we can pair a & d and b & c in an "and" statement. And to check whether any one of these and statements are true, we can just
# "or". This way, we can check if it's oppositely capitalised or not.
# After that, we can simply loop through the stack and concatenate it into the string to be returned.