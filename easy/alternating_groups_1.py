class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """

        doubled_colors = colors + colors
        alternating_groups = 0

        for right in range(0, len(colors)):
            if doubled_colors[right] != doubled_colors[right+1] and doubled_colors[right+1] != doubled_colors[right+2]:
                alternating_groups += 1

        return alternating_groups

# So we can see if it's an alternating group if right is not the same as what's next to it, and if what's next to right is not the same as what's
# next to even it.
# Consider 010. 0 is not the same as 1, and 1 is not the same as 0.
# The problem is, we are bound by the index going out of bounds. The way we can solve that is just doubling colors into an extended
# doubled_colors array, and we can then just loop right from 0->len(colors). So if we have a colors array [0,1,0,0,1], then looping from 0 till 4,
# would give us [1] and in the doubled_colors array [0,1,0,0,1,0,1,0,0,1] we could check doubled_colors[5] and [6] too.