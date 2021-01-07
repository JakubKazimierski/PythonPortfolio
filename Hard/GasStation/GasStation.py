'''
Gas Station from Coderbyte
January 2021 Jakub Kazimierski
'''

import sys

def GasStation(strArr):
    '''
    Have the function GasStation(strArr) 
    take strArr which will be an an array 
    consisting of the following elements: 
    N which will be the number of gas stations in 
    a circular route and each subsequent element will 
    be the string g:c where g is the amount of gas in 
    gallons at that gas station and c will be the amount 
    of gallons of gas needed to get to the following gas station.

    For example strArr may be: ["4","3:1","2:2","1:2","0:1"]. Your goal 
    is to return the index of the starting gas station that will allow you 
    to travel around the whole route once, otherwise return the string 
    impossible. 
    
    For the example above, there are 4 gas stations, and your program should 
    return the string 1 because starting at station 1 you receive 3 gallons 
    of gas and spend 1 getting to the next station. Then you have 2 gallons 
    + 2 more at the next station and you spend 2 so you have 2 gallons when 
    you get to the 3rd station. You then have 3 but you spend 2 getting to the 
    final station, and at the final station you receive 0 gallons and you spend 
    your final gallon getting to your starting point. Starting at any other gas 
    station would make getting around the route impossible, so the answer is 1. 
    If there are multiple gas stations that are possible to start at, return the 
    smallest index (of the gas station). N will be >= 2.
    '''
    
    gas_stations = int(strArr[0])

    stations = []
    possible_roads = []

    for gain_loss in strArr[1:]:
        stations.append((int(gain_loss.split(":")[0]), int(gain_loss.split(":")[1])))

    def trip(stations, station_id, road, gas):
        '''
        Returns None if it is impossible to cycle all stations,
        else return list of stations_id in order of visited.
        '''
        road.append(station_id)

        # if not full cycle is made
        if len(road) < gas_stations + 1:
            gain = stations[station_id][0]
            cost = stations[station_id][1]
            if len(gas) != 0:
                after_trip = gain - cost + gas[-1] 
            else:
                after_trip = gain - cost
            
            # append amount of left gas
            gas.append(after_trip)

            if after_trip >= 0:
                # ((station_id+1) % gas_stations) makes full cycle to index 0
                trip(stations, ((station_id+1) % gas_stations), road, gas)
         
        return road if len(road) == gas_stations + 1 else None

    for station_id in range(len(stations)):
        possible_roads.append(trip(stations, station_id, [], []))

    for road in possible_roads:
        if road != None:
            # due to indexing from 0 increment output
            return road[0] + 1        

    return "impossible"    
