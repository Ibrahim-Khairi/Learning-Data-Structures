class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        match_flag = True
        char_pointer = 0
        stack = []

        while char_pointer <= len(s)-1 and match_flag:
            if s[char_pointer] in ["(", "[", "{"]:
                stack.append(s[char_pointer])
            elif s[char_pointer] in [")", "]", "}"]:
                if s[char_pointer] == ")":
                    if len(stack) > 0 and stack[-1] == "(":
                        match_flag = True
                        stack.pop()
                    else:
                        match_flag = False
                elif s[char_pointer] == "]":
                    if len(stack) > 0 and stack[-1] == "[":
                        match_flag = True
                        stack.pop()
                    else:
                        match_flag = False
                elif s[char_pointer] == "}":
                    if len(stack) > 0 and stack[-1] == "{":
                        match_flag = True
                        stack.pop()
                    else:
                        match_flag = False
            char_pointer += 1

        if len(stack) > 0:
            return False
        else: 
            return match_flag

# If you think about it, the order that things need to be closed in tells you about what we can use for this problem.
# That's right. We need a stack, since the last thing opened needs to be the first thing closed.
# First thing, we need is a flag to determine if the brackets are matching. We also obviously need a pointer that goes through the string.
# An empty stack is going to be used for our reference.
# If there's any opening brackets - (, [, { - then we will push them onto the stack.
# For any closing brackets - ), ], } - we will check them against their relevant pairs. So ) will be checked against (, and so on.
# If there's an element in the stack, and it's the corresponding opening bracket, then the flag will remain true, and we can pop out that
# opening bracket specifically.
# If not, then the match flag becomes false, and we quit the loop.
# There's one specific problem if there's still remaining brackets in the loop after we are done iterating through the string, meaning those
# brackets never got closed. Hence, we can just say they don't have a match, and return False. Otherwise, we can return the match_flag as is.
# By the way. Any array[-1] just iterates to their last element. Meaning if an array is [1,2,3] then [-1] would return 3. Therefore, we can
# take a peek at the last element or bracket of the stack through [-1]. Should have probably told this earlier but yeah.