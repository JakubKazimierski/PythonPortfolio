'''
Codility 1 task February 2021
Jakub Kazimierski
'''

def solution(S, T):


    start_list = [int(elem) for elem in S.split(":")]
    end_list = [int(elem) for elem in T.split(":")]


    def check_set(hours, minutes, seconds):

        string_hours = str(hours)
        string_minutes = str(minutes)
        string_seconds = str(seconds)

        # assert format HH:MM:SS
        if len(string_hours) < 2:
            string_hours = '0' + string_hours
        if len(string_minutes) < 2:
            string_minutes = '0' + string_minutes
        if len(string_seconds) < 2:
            string_seconds = '0' + string_seconds


        total_time = string_hours + string_minutes + string_seconds

        if 1<= len(set(total_time)) <= 2:
            return True

        return False

    def timer(start, end, interesting_points):

        hours_s = start[0]
        minutes_s = start[1]
        seconds_s = start[2]

        hours_e = end[0]
        minutes_e = end[1]
        seconds_e = end[2]
          
        while hours_s <= hours_e and minutes_s <= minutes_e and seconds_s <= seconds_e:
            
            if check_set(hours_s, minutes_s, seconds_s):
                interesting_points += 1

            if seconds_s == 60:
                minutes_s += 1
                seconds_s = 0

            if minutes_s == 60:
                hours_s += 1
                minutes_s = 0

            if hours_s == 24:
                hours_s = 0        

            seconds_s += 1

        return interesting_points

    interesting_points = timer(start_list, end_list, 0)

    return interesting_points