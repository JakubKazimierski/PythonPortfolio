'''
Valid IP Addresses from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def validIPAddresses(string):
    '''
    You're given a string of length 12 
    or smaller, containing only digits. 
    Write a function that returns all the 
    possible IP addresses that can be created by
    inserting three '.'s in the string.

    
    An IP address is a sequence of four positive 
    integers that are separated by '.'s, where
    each individual integer is within the range
    0-255, inslusive.

    An IP addresses isn't valid if any of the 
    individual integers contains leading 0s. For
    example, "192.168.0.1" is a valid IP address, but
    "192.168.00.1" and "192.168.0.01" aren;t, because
    they contain "00" and 01, respectively. Another
    example of a valid IP address is "99.1.1.10";
    conversely, "991.1.1.0" isn't valid, because "991"
    is greater than 255.
    
    Your function should return the IP addresses in 
    string format and in no particular order. If no 
    valid IP addresses can be created from the string,
    your function should return an empty list.
    '''

    # helper method
    def isValidPart(string):
        '''
        O(n) time where n is length of string
        O(1) space
        Returns True if part of IP addres is valid
        else False.
        '''
        string_to_int = int(string)
        if string_to_int > 255:
            return False

        # if has leading 0's IP is not valid    
        return len(string) == len(str(string_to_int))

    # O(1) time | O(1) space (due to num of IP addresses is constant)
    ipAddressesFound = []

    # in order not to have out of range error
    # also range is from 1, cause '.' cannot appear before num
    for idx_1 in range(1, min(len(string), 4)):
        currentIPAddressParts = ['', '', '', '']

        currentIPAddressParts[0] = string[:idx_1]
        if not isValidPart(currentIPAddressParts[0]):
            continue

        for idx_2 in range(idx_1+1, idx_1 + min(len(string)-idx_1, 4)):
            currentIPAddressParts[1] = string[idx_1:idx_2]
            if not isValidPart(currentIPAddressParts[1]):
                continue

            for idx_3 in range(idx_2+1, idx_2 + min(len(string)-idx_2, 4)):
                currentIPAddressParts[2] = string[idx_2:idx_3]
                currentIPAddressParts[3] = string[idx_3:]
                if isValidPart(currentIPAddressParts[2]) and isValidPart(currentIPAddressParts[3]):
                    ipAddressesFound.append('.'.join(currentIPAddressParts))


    return ipAddressesFound
