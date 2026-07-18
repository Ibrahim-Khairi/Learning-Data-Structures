class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # First loop -> We set all the negatives to 0
        for x in range(len(nums)):
            if nums[x] < 0:
                nums[x] = 0

        # Second loop -> This loop is where we figure out whether to set specific numbers to negatives - which is going to help us in
        # deciding whether the indices for those exist or not
        for x in range(len(nums)):
            element = abs(nums[x])
            if 1 <= element <= len(nums):
                if nums[element-1] > 0:
                    nums[element-1] *= -1
                elif nums[element-1] == 0:
                    nums[element-1] = (len(nums)+1) * -1

        # Third loop -> The final loop where we decide whether the element we are iterating over exists or not in the array. If the computed
        # index for that number happens to be greater than 0, that means that number doesn't exist since essentially we are going from
        # smallest to biggest. Otherwise, we'll end up with the worst case scenario which is the smallest positive integer right after the
        # nums array ends (len(nums)+1)
        for x in range(1, len(nums)+1):
            if nums[x-1] >= 0:
                return x

        return len(nums)+1

# This code would've been a lot simpler, had it not been for the fact that we are restricted to O(n) time. Bruh.
# Initially, my solution was literally:
# n = 1
# while n <= len(nums)+1:
#     if n in nums:
#         n += 1
#     else:
#         return n
# return None
# But then I remembered that "if - in" basically runs an entire loop checking each element in an array from the start - which makes it a
# double nested loops algorithm. Therefore, that violates O(n) which was in fact what happened when I submitted, and it exceeded time limit.
# Therefore, I studied a solution, and this is what I came up with.
# There needs to be 3 loops -> O(n) + O(n) + O(n) => O(3n), but the constant would get ignored ultimately making it a O(n) solution.
# The first loop is meant to discard all negatives that originally exist in the input array. We need to change all the negatives to 0, since
# that's the most neutral value. Making it any positive integer would alter the input set that we have to compute a solution for. And ofcourse,
# any 0 that already exists, we can just keep that as is.
# That's fairly simple, we can just iterate over each element, find which one's less than 0, and just make it 0.
# The second loop is the most toxic one. Basically, we need to go through each element, and take out it's absolute value. The reason being
# we need to compute the supposed index from this absolute value which is otherwise not possible if it were to be a negative.
# We would then check whether the absolute value lies within the bounds of 1 -> len(nums).
# This is because, the smallest positive integer we are starting with is 1, and the next smallest positive integer that we could possibly have
# within the means of what's possible in the array is the length of the array itself. So consider [2,3,0]. In this array, the smallest
# positive integer that we are missing is 1. How do we know that? Well, 1 is the smallest positive integer in itself, and it's not there in the
# array, therefore, that's literally the answer. Now consider [1,2,4]. The smallest positive integer -> 1, that exists. The next -> 2, that
# exists. The next -> 3, that does not exist. Anything after 4 is just automatically violating the "smallest" rule.
# So now that the bounds are in place, if the absolute value is in those bounds, then we need to compute its index. The way we can do that is
# through just subtracting it by 1 and then using that result post-subtraction as the index that we have to work with. Basically,
# Consider an array [3,5,7,1]. The bounds, starting from 1, would make out to be 1,2,3,4 (1->len(nums)). Therefore, to link the bounds with the
# array itself, we can just say that 1-1 is 0, so nums[1-1] is 3. Similarly, nums[2-1] is 5, nums[3-1] is 7, and nums[4-1] is 1. Therefore, now
# with these computed indices we need to figure out whether the value has to be made a negative or not. This is because if that value is positive,
# and within the bounds we previously talked about - once made negative, would let us decide whether that number exists in the array or not. If
# a number was already negative before, and we made it into 0, the only and safest option is to make it a negative out of the bounds of the
# array, which is len(nums)+1.
# So imagine an array [3,4,-1,1]. The first loop would make the -1 into a negative, therefore making it out to be [3,4,0,1]. Now the second loop
# would take each value and see whether it's in the bounds of the array. If it is, then it's just made negative. 3,4,1 are all within the bounds
# 1->len(nums), therefore all of those would be made into negatives this time around. Taking the absolute of an element also helps with any
# "manually-made" negatives. For the 0, we can't make it -1,-2, or whatever because that would violate our input array once we take the absolute.
# Therefore, len(nums)+1 -> 5 is the only negative that we can assign to it. The computed array would now look like [-3,-4,-5,-1].
# Now the final loop basically iterates over the bounds themselves (1->len(nums)+1), trying to compute whether the iterable linked to those bounds
# is a negative or not. If it's a negative, that means it exists in the array. If it's still a 0 or a positive, then that specific index does not
# exist, so we can just return that.
# In this array, it would go over 1 (-3) and say it exists, therefore it would just skip that bound. Then it would go over 2 (-4) and say it
# exists, skipping that bound. Up until now, bounds 3 and 4 exist in the array. 3 (-5) exists, and finally 4 (-1) exist. Therefore, bounds
# 1,3,4,5 are all the ones that exist. Leaving, us with the one and only 2.