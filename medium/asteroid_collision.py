asteroids = [5,10,-5]

stack = [asteroids[0]]
for x in range(1, len(asteroids)):
    resolved_flag = False
    while not resolved_flag:
        if len(stack) > 0:
            a = stack[len(stack)-1]
            b = asteroids[x]
            if a < 0 and b < 0:
                stack.append(b)
                resolved_flag = True
            elif a > 0 and b > 0:
                stack.append(b)
                resolved_flag = True
            elif a < 0 < b:
                stack.append(b)
                resolved_flag = True
            elif a > 0 > b:
                if a != b*-1:
                    final_asteroid = max(a, b*-1)
                    if final_asteroid == b*-1:
                        stack.pop()
                    else:
                        resolved_flag = True
                else:
                    stack.pop()
                    resolved_flag = True
        else:
            stack.append(asteroids[x])
            resolved_flag = True
print(stack)

# So my first approach was something like this. However, there was a problem in it. It wasn't re-doing any checks if the asteroid that
# came in was a collision one which was bigger. For example in the case of 3, 2, -6. -6 would first collide with 2 and destroy it. That was
# accounted for in this solution. However, later it wouldn't check for 3 and -6, which would well happen and -6 would destroy 3 too.
# for x in range(0, len(asteroids)):
#     if len(stack) == 0:
#         stack.append(asteroids[x])
#     else:
#         stack_asteroid = stack[len(stack)-1]
#         asteroids_asteroid = asteroids[x]
#         if (stack[len(stack)-1] < 0 < asteroids[x]) or (stack[len(stack)-1] > 0 > asteroids[x]):
#             if stack[len(stack)-1] < 0:
#                 stack_asteroid = stack[len(stack)-1] * -1
#             else:
#                 asteroids_asteroid = asteroids[x] * -1
#
#             if stack_asteroid <= asteroids_asteroid:
#                 stack.pop()
#
#         else:
#             stack.append(asteroids[x])
# Therefore, I had to get the same x < 0 < y or x > 0 > y approach, just in a while loop. Hence, the second/final solution.
# The first thing I do is add in the first asteroid to the stack either way and start going from the second element in the asteroids list.
# Then I keep a flag that initially stays False and the loop keeps running as long as its False, the second it's True, the loop exits, and we
# move on towards the next asteroid.
# Inside the while loop, there's two conditions. If the stack is empty, then it'll simply append the incoming asteroid. Otherwise, it has
# multiple cases to account for.
# The first thing we do is set two variables. a being the top of our stack that we're maintaining, and b being the incoming asteroid.
# If both a and b are negative (both are moving leftwards), then we can just append the incoming asteroid since they don't collide.
# Similarly, if both a and b are positive (both are moving rightwards), then we can append the incoming asteroid again since they don't
# collide.
# The next two cases are what matter the most.
# If the top of our stack (the already existing asteroid) is negative (going leftwards), and the current asteroid (incoming asteroid) is
# positive (going rightwards), then they'll never meet.
# <- a | b ->
# Therefore, we can just append the incoming asteroid as is.
# The final case is one where we already have a positive asteroid (one going rightwards), and the incoming asteroid (going leftwards) is
# what we have to deal with. Here the collision scene happens.
# The first thing we do is check whether their values are the same. If 5 and -5 collide, since they both are the same values, they'll just
# destroy each other, and we'll be left with nothing. Also, to get a positive equivalent of a leftwards incoming asteroid, we can just
# multiply it with -1. Building on that, we see if they are both equal. If not, we never append the incoming asteroid since we set the flag
# to true, meaning the while loop can exit, and the next asteroid can continue on, and pop out the asteroid in our stack already. In the
# case where they are equal, we take the max out of them after removing the signs again. If this final asteroid happens to be the positive
# form of b, it means b won (since we can just negate the sign syndrome because it specifies direction instead of value greatness). In the
# case that b won, we can just remove the already existing asteroid but not append b just yet because it still needs to check with the
# remaining asteroids in the stack. If a wins, then we just don't need to do anything since b is destroyed, and we don't need to append it.
# Therefore, we set the resolve_flag to true.
# I loved this problem, it was so aesthetic man.