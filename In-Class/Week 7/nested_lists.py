# NAME: Omar Salah
# ID: 5970678517
# DATE: 2022-09-28
# DESCRIPTION:IN class assignment for Monday October 3 2022. Just a couple simple functions to test our knowledge on nested loops
#   One iterates through a list of strings isolating digits within each string to be summed and another just checks if 2 coins
#   could be used to pay for an item evenly

from math import remainder
from typing import List
from functools import reduce

def digital_sum(nums_list: List[str]) -> int:
    """Return the sum of all the digits in all strings in nums_list.

    Precondition: s.isdigit() holds for each string s in nums_list.

    >>> digital_sum(['64', '128', '256'])
    34
    >>> digital_sum(['12', '3'])
    6
    """
    #  I Could do this with nested reduces but instead I am going to just do a quick set of nested for loops

    # To start I am going to start by initiating the total to be 0. This will serve to allow us to add each digit to the total

    # First for loop is going to pull each individual digit string from the input list and pass that to our second nested loop
    # The second nested loop is then going to take each string and split it into individual digits which will then be individualy type cast to int 
    #   and added to our running total. We just return it after that

    total = 0
    for str in nums_list:
        for digit in str:
            total += int(digit)
    return total



def can_pay_with_two_coins(denoms: List[int], amount: int) -> bool:
    """Return True if and only if it is possible to form amount, which is a 
    number of cents, using exactly two coins, which can be of any of the 
    denominatins in denoms.
    
    >>> can_pay_with_two_coins([1, 5, 10, 25], 35)
    True
    >>> can_pay_with_two_coins([1, 5, 10, 25], 20)
    True
    >>> can_pay_with_two_coins([1, 5, 10, 25], 12)
    False
    """

    # Keeping time space efficiency in mind, we should really be able to tell if we can get change in 2 coins with no more than 2 passes.
    # That being said We can just inject this as a condition and use it in creating logic to return

    #  First we initiate a counter to count the coins returned and limit us to only 2 and a remainder which will be the change remaining after
    #   Each respective coin is given out
    # Our return condition can then simply be to check if their is still a remaining balance in remainder after using the 2 larges possible denominations
    #   That would apply to the ammount giver
    count, remainder = 0, amount

    # Iterate through each of the denominations from largest to smallest 
    for denom in denoms[::-1]:

        # Basically check while our remainder is less than the coin we are looking at, and we have not exceeded the max coins we can return
        #   we can subtract this denom from the remainder as many times as we can without going negative ensuring we are always using the largest po
        #   possible denominations for change
        while remainder >= denom and count < 2:
            remainder-=denom
            count+=1
    # Now we can simply return whether or not any change is remaining due which would mean that we could not use 2 coins to pay
    return not remainder





def main():
    # Generic test cases from the doc strings. I will basically always do something like this if not outright create a repl or interface to test 
    #   functionality, so I would like to stop commenting on these.
    print(digital_sum(['64', '128', '256']))
    print(digital_sum(['12', '3']))

    print(can_pay_with_two_coins([1, 5, 10, 25], 35))
    print(can_pay_with_two_coins([1, 5, 10, 25], 20))
    print(can_pay_with_two_coins([1, 5, 10, 25], 12))

if __name__ == "__main__":
    main()
