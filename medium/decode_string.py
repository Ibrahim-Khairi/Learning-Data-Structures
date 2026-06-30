class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        num_array = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        stack = []

        for x in range(0, len(s)):
            if s[x] != "]":
                stack.append(s[x])
            else:
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()

                multiply_num = ""
                while stack and stack[-1] in num_array:
                    multiply_num = stack.pop() + multiply_num

                for y in range(0, int(multiply_num)):
                    stack.append(substring)

        result_string = ""
        for x in stack:
            result_string += x

        return result_string

# So you keep appending everything into the stack that's not a closing bracket.
# The second we find a closing bracket, it means we need to resolve that substring. To do that, we'll keep popping out of the stack, till we
# hit the opening bracket for that closing bracket. Every character that we pop, we add to the FRONT of our substring. When we do reach the
# opening bracket, we get out of the loop and then pop one final time to remove the "]".
# Once we've finalized the substring, we need to get the integer behind it. In other words, we need to get the value by which we'll decide
# how many times it has to repeat. To do that we simply need to see which characters are numbers. So lets say our stack looks like
# ... a, ], 6, [b, c] (... represents the previous values). Now here the substring would become bc. We'll keep moving backwards until we
# find a char that's not a number. "6" is a number. "]" is not a number. We also need to make sure the stack is not empty already. Then we
# can finally come up with the multiply_num.
# Once we have the multiply_num, we just run a for loop for that iterations and keep concatenating the characters into a result_string that
# will eventually be returned.