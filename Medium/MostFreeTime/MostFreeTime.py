'''
Most Free Time from Coderbyte
December 2020 Jakub Kazimierski
'''

from datetime import datetime

def grouped(iterable, n):
    #s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ...
    return zip(*[iter(iterable)]*n)

def MostFreeTime(strArr):
    '''
    Have the function MostFreeTime(strArr) 
    read the strArr parameter being passed 
    which will represent a full day and will 
    be filled with events that span from time 
    X to time Y in the day. The format of each 
    event will be hh:mmAM/PM-hh:mmAM/PM. 
    
    For example, strArr may be 
    ["10:00AM-12:30PM","02:00PM-02:45PM","09:10AM-09:50AM"]. 
    Your program will have to output the longest amount of free 
    time available between the start of your first event and the 
    end of your last event in the format: hh:mm. 
    The start event should be the earliest event in the day and 
    the latest event should be the latest event in the day. 
    The output for the previous input would therefore be 01:30 
    (with the earliest event in the day starting at 09:10AM and 
    the latest event ending at 02:45PM). The input will contain 
    at least 3 events and the events may be out of order.
    '''

    FMT = '%I:%M%p'
    times = []
    breaks = []

    for period in sorted(strArr):
        start = datetime.strptime(period.split("-")[0], FMT)
        stop = datetime.strptime(period.split("-")[1], FMT)

        times.extend([start, stop])

    times = sorted(times)

    # count diffs between end of one piriod and start of next one
    # start time of day and stop are not needed to be included
    for start_break, stop_break in grouped(times[1:-1], 2):
        tdelta = stop_break - start_break
        breaks.append(tdelta)

    max_break = max(breaks)

    hours = int(max_break.seconds/3600)
    minutes = int(max_break.seconds/60) - hours*60

    hours = str(hours) if hours > 9 else "0"+str(hours)
    minutes = str(minutes) if minutes > 9 else "0"+str(minutes)

    return ":".join([hours, minutes])