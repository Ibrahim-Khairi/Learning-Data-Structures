class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = []
        current = 0
        operator = "+"

        for x in range(0, len(s)):
            char = s[x]
            if char.isdigit():
                current = current * 10 + int(char)

            if char == "*" or char == "/" or char == "+" or char == "-" or x == len(s) - 1:
                if operator == "+":
                    stack.append(current)
                elif operator == "-":
                    stack.append(-current)
                elif operator == "*":
                    stack[-1] *= current
                elif operator == "/":
                    stack[-1] = int(stack[-1] / float(current))

                current = 0
                operator = char

        return sum(stack)

# So the most challenging part in this problem is the fact that we need to follow Operator Precedence, or BODMAS.
# Initially, we'll declare stack as empty, current as 0, and operator as +.
# The stack is basically where we'll send all numbers that are NOT being multiplied or divided, to be computed. The default operation
# for the stack is summation, therefore, once we find a number that has to be multiplied, we'll just immediately multiply it, and then
# append that multiplication onto the stack. Same thing with division.
# If we see a subtraction, then we'll just append the subtractor symbol with the number itself. During the time of summation, it'll
# automatically be subtracted because + - makes -.
# We'll go through each char in the string. If the char happens to be a digit, then we can just perform a "concatenation" of sorts to
# current. Basically current = current * 10 + int(char) is a way of building up a multi-digit number one character at a time.
# Let's say current = 0, and we have to deal with "197".
# current = 0 * 10 + 1 = 1
# current = 1 * 10 + 4 = 14
# current = 14 * 10 + 2 = 142
# Therefore, through that we can just keep adding digits to current until we get a finalized number.
# The second we hit an operator or if we hit the last iteration, we'll do the actual computation for all 4 testcases of the operators.
# 1) If the operator is +, we can just simply append it into our stack, which is automatically set on summation.
# 2) If the operator is -, we can just simply append it with a subtraction symbol in front of it into our stack.
# 3) If the operator is either * or /, we need to take the number at the top of the stack and multiply or divide it with current.
# The division part is what caught me off guard. Simple floor division doesn't work in Leetcode's python 2 or whatever, so I had to do
# float(current) and then i had to do int() across all of that.
# After that we can just reset the values to default normally, so we can set current to 0 and operator to char.