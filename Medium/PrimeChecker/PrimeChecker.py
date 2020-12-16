'''
Prime Checker from Coderbyte
December 2020 Jakub Kazimierski
'''
from math import sqrt
from itertools import permutations, count, islice

def is_prime(num):
    
    # isslice only needs to memorize the initial arguments you provide
    # and generates every number on-the-fly
    # if num%i == 0 then bool(0) == False

    return num > 1 and all(num % i for i in islice(count(2), int(sqrt(num)-1)))

def PrimeChecker(num):
    '''
    Have the function PrimeChecker(num) 
    take num and return 1 if any arrangement 
    of num comes out to be a prime number, 
    otherwise return 0. 
    
    For example: if num is 910, the output should 
    be 1 because 910 can be arranged into 109 or 019, 
    both of which are primes.
    '''
    
    num_permutations = list(int("".join(permutation)) \
        for permutation in set(permutations(str(num), len(str(num)))))

    for permutation in num_permutations:
        if is_prime(permutation):
            return 1

    return 0
