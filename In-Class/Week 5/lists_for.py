# NAME: Omar Salah
# ID: 5970678517
# DATE: 2022-09-26
# DESCRIPTION: Simple code to test the usage of for in loops and basic list comprehension using the [start Index: End Index: Step] syntax


from typing import List


def collect_below_threshold(nums: List[int], threshold: int) -> List[int]:
    """Return a new list consisting of those numbers in nums that are below
    threshold, in the same order as in nums.
    
    >>> collect_below_threshold([1, 2, 3, 4], 3)
    [1, 2]
    >>> collect_below_threshold([1, 2, 108, 3, 4], 50)
    [1,2,3,4]
    >>> collect_below_threshold([], 7)
    []
    """
    # Here is the method you would expect to see from class. Originally we initialize an empty list called ret, what we will do 
    # from here is simply iterate over each item in the list of nums we recieved as an argument, and append the items that happen 
    # to be less than threshhold
    ret = []
    # Here is a very simple exit case that checks to see if our input is empty, if that is the case then we simply return the empty list otherwise we get to do the actual work
    if not len(nums):
        return []
    # Here we are iterating over each item in our input list, and testing to see if it is less than or greater than the threshold
    # if it is lest, we will append that value directly to the ret list which we will be returning
    for num in nums:
        if num < threshold:
            ret.append(num)
    # Now that we have finished iterating everything we can simply return the list we created
    return ret

    # This works the same way except we use filter instead of iterating through the loop manually. Filter returns a second list
    # of only items that return true when checked the syntax is filter(Function -> boolean, iterable). In which case we filter
    # through the iterable item by item being passed to the function. Only cases that return true will be added to the list returned by filter

    # I used a lambda function here since there is no point in using up extra space and memory to define such a simple function. 
    # we are just comparing each number to the threshhold if it is less than, it will be added to the return list, otherwise we just move on.
    return filter(lambda num: num < threshold, nums)


def scale_midterm_grades(grades: List[int], multiplier: int, bonus: int) -> None:
    """Modify each grade in grades by multiplying it by multiplier and then
    adding bonus. Cap grades at 100.
    
    >>> grades = [45, 50, 55, 95]
    >>> scale_midterm_grades(grades, 1, 10)
    [55, 60, 65, 100]
    >>> grades = [95, 100, 20, 30, 40, 50, 90, 80]
    >>> scale_midterm_grades(grades, 2, 5)
    [100, 100, 45, 65, 85, 100, 100, 100]
    >>> grades = []
    >>> scale_midterm_grades(grades, 10, 10)
    []
    """
    #  Just some quick exception handling in the case we recieve and empty array,there is no point in doing anything else, 
    #  Jus return another empty array
    if not len(grades):
        print([])

    # Here we are iterating over each item in our input list, and calculating what the modified grade would be. We can then
    # Simply find the minimum 
    for i, grade in enumerate(grades):
        grades[i] = min((grade*multiplier)+bonus, 100)
    # Really just turning this into a single pretty string that we can output
    print("".join([str(grade) + ", " for grade in grades])+"]")




    # This will do the same thing as above just all in one line and alittle cleaner. We just map over the grades creating a new 
    #  array of the modified grades that we then join into a single pretty string that is being printed

    # print("".join([map(lambda grade: min(grade*multiplier+bonus, 100), grades)])) 

# Complete the following
def main():
    # Just defining the same test cases as above so that you know what the expected output is for testing below threshold
    belowThresh1 = collect_below_threshold([1, 2, 108, 3, 4], 50)
    belowThresh2 = collect_below_threshold([1, 2, 3, 4], 3)
    belowThresh3 = collect_below_threshold([],7)
    print("Testing Below threshold1: \n")
    for num in belowThresh1:
        print(num)
    print("Testing Below threshold2: \n")
    for num in belowThresh2:
        print(num)
    print("Testing Below threshold3: \n")
    for num in belowThresh3:
        print(num)

    # Same as above just defining and running test cases.
    grades1 = [45, 50, 55, 95]
    print("Testing Scaling grades1: \n")
    scaledGrades1 = scale_midterm_grades(grades1, 1, 10)
    grades2 = [95, 100, 20, 30, 40, 50, 90, 80]
    print("Testing Scaling grades2: \n")
    scaledGrades2 = scale_midterm_grades(grades2, 2, 5)
    grades3 = []
    print("Testing Scaling grades3: \n")
    scaledGrades3 = scale_midterm_grades(grades3, 10, 10)





if __name__ == "__main__":
    main()


