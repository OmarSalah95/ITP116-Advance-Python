# NAME: Omar Salah-Eddine
# ID: 5970678517
# DATE: 2022-09-03
# DESCRIPTION: I am not super sure what kind of course description would be needed here... I thin the comments in all the tasks about cover it
#       It is a console app that takes user inputs that are used when invoking our newly defined functions. 

from cmath import pi
import math


# Task 1
# Complete function double so that it takes a number and returns twice its value
# according to the examples in the docstring. Use a return statement; note that
# this function does not have a print statement.
def double(num: float) -> float: return 2*num




# Task 2
# Function our_maximum takes two numbers and returns the larger of the two.
# Complete the function.
def our_maximum(num1: float, num2: float) -> float: return max(num1,num2)
# Another method of doing it
# num1 if num1 > num2 else num2




# Task 3
# Complete the following function.
def max_of_min(num1: float, num2: float, value1: float, value2: float) -> float: return max(min(num1, num2), min(value1, value2))
    # """Return the maximum of the minimums of the pairs num1 and num2,
    # and value1 and value2.
    # >>> max_of_min(4.0, 3.7, 6.0,3.5)
    # 3.7
    # >>> max_of_min(1, 1.7, 4.5, 3.0)
    # 3.0
    # """



# Task 4
# Function format_name receives two parameters.
# The first parameter represents a first name and the second represents a last name.
# It returns a string in the format: last_name, first_name
# where last_name and first_name are replaced by the given last and first names.
def format_name(first_name: str, last_name: str) -> str: return ", ".join((last_name.capitalize(), first_name.capitalize()))

# last_name.capitalize() + ", " + first_name.capitalize() is another method that is easy



# Task 5
# Complete the following function circle_area.
# It receives the radius and returns the area of the circle.
# Add proper comments.
def circle_area(radius: float) -> float: return float(math.pi) * (radius** 2)


# Task 6
# Function sum_to receives one parameter
# the parameter is a number
# returns an integer value: the sum of all integers from 1 to that number
# Add proper comments.
def sum_to(n: int) -> int: return sum(range(1,n+1))


# Task 7
# Complete function is_odd which receives one parameter.
# the parameter is a number.
# returns a boolean value True if the number is odd and False otherwise.
# Add proper comments.
def is_odd(n: int) -> bool: return bool(n % 2) 


# Task 8
# Complete function is_even which receives one parameter.
# the parameter is a number.
# returns a boolean value True if the number is even and False otherwise.
def is_even(n: int) -> bool: return not bool(n % 2)


# Complete calling
def main():
    print("Starting task 1, doubling a number.")
    num_to_double = input("Please enter the number you would like to duplicate: ")
    print("Double of", num_to_double, "is", double(float(num_to_double)))
    input("Press any key to continue...\n")

    print("Starting task 2, finding maximum.")
    first_num = input("Please enter the first number: ")
    second_num = input("Please enter the second number: ")
    print("Max of", first_num, "and", second_num, "is", our_maximum(float(first_num), float(second_num)))
    input("Press any key to continue...\n")

    print("Starting task 3, finding max of min.")
    user_num1 = input("Please enter the a value for num1: ")
    user_num2 = input("Please enter the a value for num2: ")
    user_value1 = input("Please enter the a value for value1: ")
    user_value2 = input("Please enter the a value for value2: ")
    print("Max of min of pairs (" + user_num1 + "," + user_num2 + ") and (" +
        user_value1 + "," + user_value2 + ") is ",
        max_of_min(float(user_num1), float(user_num2), float(user_value1), float(user_value2)))
    input("Press any key to continue...\n")

    print("Starting task 4, format name.")
    first_num = input("Please enter the first name: ")
    second_num = input("Please enter the last name: ")
    print(format_name(first_num, second_num))
    input("Press any key to continue...\n")

    print("Starting task 5, finding area of circle.")
    # Task 9
    # provide the code for calling function circle_area
    rad = int(input("Please enter a radius: "))
    print(circle_area(rad))
    input("Press any key to continue...\n")

    print("Starting task 6, finding Summation of n.")
    to_sum_up_to = input("Please enter the number you'd like to sum up to: ")
    print("Summing up to ", to_sum_up_to, "yields", sum_to(int(to_sum_up_to)))
    input("Press any key to continue...\n")

    print("Starting task 7 checking odd:")
    user_input = input("Please enter the number you'd like to check: ")
    print("It is", is_odd(float(user_input)), "that", user_input, "is odd.")
    input("Press any key to continue...\n")

    print("Starting task 8 checking odd:")
    # Task 10
    # provide the code for calling function is_odd 

    # not sure if this should be calling the function is even considering that we tested get odd in the line above. I will just go ahead and test get even
    temp = int(input("Enter the number you would like to test(Is even)"))
    print(is_even(temp))
    input("Press any key to continue...\n")

# Do not change
if __name__ == "__main__":
    main()
