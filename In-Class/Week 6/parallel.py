# NAME: Omar Salah
# ID: 5970678517
# DATE: 2022-09-28
# DESCRIPTION:IN class assignment for Wednesday 28 2022. Just a couple simple functions to stretch a string character by character
#   by multiplying each char by some factor, and the second is to find the largest difference between matching values in 2 
#   arrays 
from typing import List


def stretch_string(s: str, stretch_factors: List[int]) -> str:
    """Return a string consisting of the characters in s in the same order as in s,
    repeated the number of times indicated by the item at the corresponding
    position of stretch_factors.
    
    Precondition: len(s) == len(stretch_factors) and the values in
                stretch_factors are non-negative
    
    >>> stretch_string('Hello', [2, 0, 3, 1, 1])
    'HHllllo'
    >>> stretch_string('echo', [0, 0, 1, 5])
    'hooooo'
    """
    # So Since this is 1 line, we can go step by step
    # First we are taking an empty string that we are going to return and joining the rest of the return string to it as
    #   it is processed. Join allows us to join sub-strings together.
    # Then, we enumerate our string. Enumerate takes an iterable object like a string and creates a dictionary with the
    #   the index of each element being stored as the key and the element itself as the value. 
    # In the for loop we then make to iterate over this dictionary, we destructure the key and value pairs into i and char
    #   I then use i as an index pointer to the relevant factor for each respective char in s.
    # It is these sub-strings of wach character multiplied by its respective factor that are then joined to the return string
    #   containing all the rest of the sub-strings before being returned as 1 string
    return "".join(stretch_factors[i]*char for i, char in enumerate(s))


def greatest_difference(nums1: List[int], nums2: List[int]) -> int:
    """Return the greatest absolute difference between numbers at corresponding
    positions in nums1 and nums2.
    
    Precondition: len(nums1) == len(nums2) and nums1 != []
    
    >>> greatest_difference([1, 2, 3], [6, 8, 10])
    7
    >>> greatest_difference([1, -2, 3], [-6, 8, 10])
    10
    """
    # Another crazy looking one liner, so we can go through step by step again :)
    # First we want to find all the difference between respective pairs of numbers in nums1 and nums2
    #   To do this I create an array of differences by first enumerating nums1 into a dictionary as before
    #   then using the index as a pointer again as above, we append the absolute value of the difference between
    #   the respective pairs of numbers. 
    # This array of absolute difference between the values is then spread into the max() function as individual arguments
    #   the spread operator for arrays is indicated by the * before map which splits the array into individual arguments 
    # we can then simply return that value
    return max(*map(lambda i_num1: abs(i_num1[1] - nums2[i_num1[0]]), enumerate(nums1)))



def main():
    # Boiler plate main stuff and test cases here. Test cases are matched to those given in doc strings
    print(stretch_string('echo', [0, 0, 1, 5]))
    print(stretch_string('Hello', [2, 0, 3, 1, 1]))
    print(greatest_difference([1, 2, 3], [6, 8, 10]))
    print(greatest_difference([1, -2, 3], [-6, 8, 10]))





if __name__ == "__main__":
    main()
