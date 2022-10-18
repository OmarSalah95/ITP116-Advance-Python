# NAME: Omar Salah
# ID: 5970678517
# DATE: 2022-09-20
# DESCRIPTION: Simple code to just take a users input string then check some of the calssification of the provided input string
# just checking if the input string is alphabetic, numberic, lower case, or upper case as well as test if the string is a plindrome
# in other words if the string is reversed is it the same as the original

def check_string(str_check: str):
    # Here we are just going to use formatted strings to inject python for logic directly in line in our print 
    # for simplicity. This method doesnt take much and allows us to execute python code in line within our string.
    print(f"Only alphabetic characters? {str_check.isalpha()}\nOnly numbers? {str_check.isdigit()}\nOnly lowercase? {str_check.islower()}\nOnly uppercase? {str_check.isupper()}\n")


def check_palindrome(str_check: str):
    # This is really simply logic, we are just comparing the string to itself when it is reversed,
    print(str_check == str_check[::-1])


def main():
    # Take input from user
    input_string = input("Enter a string: ")
    # Check the parameters we defined in check_string to give us details on the string input
    check_string(input_string)
    # tests to see if the input string is indeed a palindrom.
    check_palindrome(input_string)


if __name__ == "__main__":
    main()