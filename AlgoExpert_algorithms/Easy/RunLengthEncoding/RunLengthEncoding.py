'''
Run Length Encoding from AlgoExpert.com
January 2021 Jakub Kazimierski
'''

def runLengthEncoding(string):
    '''
    Write a function that takes in a non-empty
    string and returns its run-length encoding.

    From Wikipedia, "run-length encoding is a form of 
    lossless data compression in which runs of data
    are stored as a single data value and count, rather
    than as the original run." For this problem, a run 
    of data is any sequence of consecutibe, identical
    characters. So the run "AAA" would be run-length-encoded
    as "3A".

    To make things more complicated, however, the input string
    can contain all sorts of special characters, including numbers.
    And since encoded data must be decodalble, this
    means that we can't naively run-length-encode long runs.
    For example, the run "AAAAAAAAAAAA" (12 A's), can't naively
    be encoded as "12A", since this string can be decoded as either
    "AAAAAAAAAAAA" or "1AA". Thus, longs runs (runs of 10 or more characters)
    should be encoded in a split fashion; the aformentioned run
    should be encoded as "9A3A".    
    '''
    
    counter = 1
    output = ""

    if len(string) < 2:
        return str(counter) + string
    else:    
        for elem_id in range(len(string)-1):

            if counter < 9 and string[elem_id] == string[elem_id+1]:
                counter += 1
            else:
                output += str(counter) + string[elem_id]
                counter = 1

            if elem_id + 1 == len(string) - 1:
                if string[elem_id] == string[elem_id+1]:
                    output += str(counter) + string[elem_id]
                else:
                    output += str(counter) + string[elem_id+1]
                    
        return output

