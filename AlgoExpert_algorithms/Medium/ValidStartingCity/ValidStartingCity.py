'''
Valid Starting City from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def validStartingCity(distances, fuel, mpg):
    '''   
    Imagine you have a set of cities that are laid out 
    in a circle, connected by a circular road that runs 
    clockwise. Each city has a gas station that provides
    gallons of fuel, and each city is some distance away 
    from the next city.
    
    You have a car that can drive some number of miles per
    gallon of fuel, and your goal is to pick a starting city 
    such that you can fill up your car with that city's fuel, 
    drive to the next city, refill up your car with that city's
    fuel, drive to the next city, and so on and so forth until 
    you return back to the starting city with 0 or more gallons 
    of fuel left.
    
    This city is called a valid starting city, and it's guaranteed 
    that there will always be exactly one valid starting city.
    
    
    For the actual problem, you'll be given an array of distances 
    such that city i is distances[i] away from city i+1. Since the
    cities are connected via a circular road, the last city is
    connected to the first city. In other words, the last distance 
    in the distances array is equal to the distance from the last
    city to the first city. You'll also be given an array of fuel
    available at each city, where fuel[i] is equal to the fueal
    available at city i. The total amount of fuel available (from
    all cities combined) is exactly enough to travel to all cities.
    Your fuel tank always starts out empty, and you're given a 
    positive integer value for the number of miles that your car
    can travel per gallon of fuel (miles per gallon, or MPG). You
    can assume that you will always be given at least two cities.

    Write a function that returns the index of the valid starting city.
    '''


    # greedy algorithm O(n) time | O(1) space
    # chooses city with lowest amount of miles 
    # (necessary to get there) as starting point
    # from this point gallons of gas will be enough
    # to reach each city

    min_value = 0
    city_idx = 0
    miles_left = 0

    for idx in range(len(distances)):
        # keep record of distance which we can reach from current city
        miles_left += mpg*fuel[idx] - distances[idx]

        # if possible distance is lower that current min value
        if min_value > miles_left:
            min_value = miles_left
            # city to which we going to
            city_idx = idx+1 % len(distances)

    return city_idx
