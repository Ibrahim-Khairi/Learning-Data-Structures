class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """

        string_to_stack = []
        for x in directions:
            string_to_stack.append(x)

        stack = [string_to_stack[0]]
        collision_counter = 0
        for x in range(1, len(string_to_stack)):
            resolved_flag = False
            while not resolved_flag:
                if len(stack) > 0:
                    a = stack[-1]
                    b = string_to_stack[x]
                    if a == "R" and b == "L":
                        stack.pop()
                        string_to_stack[x] = "S"
                        collision_counter += 2
                        while stack and stack[-1] == "R":
                            stack.pop()
                            collision_counter += 1
                        stack.append(string_to_stack[x])
                        resolved_flag = True
                    elif a == "R" and b == "S":
                        stack.pop()
                        while stack and stack[-1] == "R":
                            stack.pop()
                            collision_counter += 1
                        stack.append(string_to_stack[x])
                        collision_counter += 1
                        resolved_flag = True
                    elif a == "R" and b == "R":
                        stack.append(string_to_stack[x])
                        resolved_flag = True
                    elif a == "L" and b == "R":
                        stack.append(string_to_stack[x])
                        resolved_flag = True
                    elif a == "L" and b == "S":
                        stack.append(string_to_stack[x])
                        resolved_flag = True
                    elif a == "L" and b == "L":
                        stack.append(string_to_stack[x])
                        resolved_flag = True
                    elif a == "S" and b == "R":
                        stack.append(string_to_stack[x])
                        resolved_flag = True
                    elif a == "S" and b == "L":
                        string_to_stack[x] = "S"
                        stack.append(string_to_stack[x])
                        collision_counter += 1
                        resolved_flag = True
                    elif a == "S" and b == "S":
                        stack.append(string_to_stack[x])
                        resolved_flag = True
                    else:
                        break
                else:
                    stack.append(string_to_stack[x])
                    resolved_flag = True

        return collision_counter

# The first thing you would do is convert the string into a stack. Each character of the string would become an element of the stack. This is
# so that you could do assignment on a certain character/element. directions[x] doesn't allow you to do that.
# After that you declare a stack and append the first element of the string_to_stack array to it. Then you also initialise a counter.
# Afterwards, go through each element and apply the asteroid_collision.py logic. a becomes the top of the stack, and b becomes the current
# element we are processing.
# Now there's 9 possible cases.
# 1) a is R, b is L -> since both cars are colliding with each other, both will become stationery. so we can pop a out, and we'll later
# append an S instead. for b, we can just simply assign it S. however, we also need to say whether there were any pre-existing Rs in the
# stack. This is because once a turns S, the previous cars might collide with it if they are Right, so we'll run a while loop and keep seeing
# if there are Rs in the stack. Once we are done with that, we can simply append the S back in a's spot.
# 2) a is R, b is S -> a is colliding with the stationery car b. Therefore, we'll pop a out and run the previously mentioned while loop
# because after the collision a will become S therefore any previous cars moving rightwards (R) will collide with a stationery car. We can
# then safely append S.
# 3) a is R, b is R -> both cars are moving in the same direction, therefore, we can simply append b.
# 4) a is L, b is R -> both cars are moving in opposite direction, no collision. therefore, we can simply append b.
# 5) a is L, b is S -> a is moving leftwards, so it will not collide with the stationery car b. therefore, we can simply append b.
# 6) a is L, b is L -> both cars are moving in the same direction, no collision. therefore, we can simply append b.
# 7) a is S, b is R -> a is stationery, b is moving rightwards, so it will not collide with the stationery car a. therefore, we can simply
# append b as is.
# 8) a is S, b is L -> b will collide with a. Therefore, we can change b to S and then later append it.
# 9) a is S, b is S -> both cars are stationery, no collision. therefore, we can simply append b.
# Otherwise, we can just break the loop.
# If the stack is already empty, we can just append the current element as is.
# In each of the cases, we'll increment the counter depending on the situation. 2 if L R or R L collide, 1 if S L or R S collide.