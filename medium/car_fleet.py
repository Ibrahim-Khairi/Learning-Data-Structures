class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        cars = []
        for x in range(0, len(position)):
            car_prop = [position[x], speed[x]]
            cars.append(car_prop)

        cars.sort()

        times = []
        for position, speed in cars:
            time = float(target - position) / speed
            times.append(time)

        fleet = 0
        while len(times) > 1:
            top_car = times.pop()
            if top_car < times[-1]:
                fleet += 1
            else:
                times[-1] = top_car

        if times:
            fleet += 1

        return fleet

# We'll initially declare a cars list that's empty. For each car, we'll add an array/pair of position and speed in the list.
# Then, we'll sort them from the earliest position to the latest position in ascending order. This is so that our list basically has the cars in
# order.
# Moving on, we'll declare a times list that's empty. For each pair in the cars list, we'll calculate the time left until it reaches target.
# To do that, we can calculate the distance left between its current position and the target. We can do that through target - position.
# To ensure accuracy and allow for decimals, we will add a float on it. We can then divide it by speed to find out how many hours it'll take
# for the car to reach the target. We can then append this calculation in times.
# Now we have a times list with all the "time left until it reaches target" values.
# Finally, we'll initialise a fleet counter.
# We'll be comparing the first 2 elements at the top of the stack. Therefore, our while loop will be until there's only one value remaining
# in the times list.
# First, we'll pop out the top element of the stack and assign it to top_car. If top_car is less than the top of the stack (which was
# originally the second to top element), then we can simply increment the fleet by 1. This is because, top_car will take less time to reach
# the target than the second car. Hence, the second car will basically become the top now and the fleet will be incremented by one because
# the top_car would reach too fast to be part of the fleet.
# If top_car's time is bigger than the second car, then we'll just remove the second car altogether and make the top of the stack top_car's
# time. This is because the second car is faster than the top_car so it'll eventually catch up, and it's speed would fall to the speed of
# top_car. So it'll be absorbed in the fleet.
# Lastly, we'll see if there's any element/cars remaining in time. If yes, we'll just increment fleet by 1, since it will arrive by itself
# so that counts as a fleet. Otherwise, fleet will remain as is.