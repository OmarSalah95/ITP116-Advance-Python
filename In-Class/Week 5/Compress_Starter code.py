# NAME: Omar Salah
# ID: 5970678517
# DATE: 2022-09-21
# DESCRIPTION:
# Run-Length Encoding is a basic form of compression.
# RLE works by reducing the footprint of repeated character
# sequences. For example, if the decompressed string is “aaaaaaaaa”,
# the compressed string would be “9a”.
# For simplicity, you will not encounter a string with more than 9
# of the same letters in a row. In other words, there will never ever
# be a case of “aaaaaaaaaa” -> “10a”.
# This simplified RLE is less efficient when it deals with non-repeating
# character sequences. For example, “abcde” will be compressed into
# “1a1b1c1d1e”.
# This program displays a menu for the user to choose from.
# The menu and function headers are provided in this starter code.


# Complete all functions. Remember to remove extra comments.
# Remember that you need provide comments for every line of your code,
# unless it is clear what the code does.
# The output of your program should match our sample output exactly if
# the same input values are used. Test your program on multiple inputs.

# Process the string and output the compressed result.
# For compressing the string, validate that the input only contains alphabetic characters.
def compressor(decomp: str) -> str:
    if not decomp.isalpha():
        print("Only alphabetic characters are allowed when compressing a source string.")
        return ""

    charCount = {}
    ret = ""
    # In this first loop we are simply going to populate the char count dictionary with key value pairs that correspond to the 
    # characters and their respective counters
    for char in decomp:
        # if the char is already in our dictionary as an entry key with a value attached, we will simply increment the counter
        # to account for the new char
        if char in charCount:
            charCount[char] +=1
        # Otherwise, our char does not exist in our dictionary as a key, in which case we need to add it with a value of 1 representing
        # that it is the first of its kind that we have found.
        else:
            charCount[char] = 1


    # Now that we have our dictionary populated with chars and counts of each char, we can simply iterate through taking
    # said key value pairs combining them into a coefficient and a character and adding that to our return string to be printed
    for char, count in charCount.items():
        ret += str(count)+char


    # Here is another way I figured you wanted to see for class, but I also did by setting up a quick dictionary since
    # I can basicly use it as a hashtable and just use the info stored there to handle all the logic at the end after 1 pass
    # charCount = 1
    # ret = ""

    # for i, char in enumerate(decomp[1:]):
    #     if char == decomp[i-1]:
    #         charCount+=1
    #     else:
    #         ret += f"{charCount}{decomp[i-1]}"
    #         charCount = 1

    print(ret)



# For decompressing the string, validate that the input only
# contains alphanumeric characters.
# If it does, you can assume it is in the correct format
# (i.e., number followed by letter followed by number followed
# by letter, etc.).
def decompressor(comp: str) -> str:
    ret = ""
    # Confirm the input is good, otherwise we are just going to drop out of our function before wasting any time.
    if not comp.isalnum():
        print("Only alphanumeric characters are allowed when decompressing a source string.")
        return ""
    # Here we are going to use some creative logic to go through our input string that we care decompressing. 
    # since we can assume that all user input by this point will have been validated(We are assuming the data coming in is 
    # exactly what we are expecting.) While this methodology is creative starting from odd numbers and useing indexing to 
    # multiply by our chars for repeats. 
    for i in range(1, len(comp), 2):
        ret += int(comp[i-1])*comp[i]

    print(ret)



def display_menu():
    print("\nWhat would you like to do?"
        "\n1. Compress"
        "\n2. Decompress"
        "\n3. Exit\n")


# The program will first ask the user if she would like to
# compress or decompress a string.
# After the result is printed, loop back to the main menu.
# Only quit the program when the user selects the exit option
# in the menu.
def receive_choice() -> str:
    display_menu()
    user_choice = input("Your choice: ")
    while user_choice not in ['1', '2', '3']:
        print("That is not a valid option."
            "\n---\n")
        # This was missing a tie in to the while condition so that we can escape the loop. Otherwise without this we will
        # get a nasty infinite loop
        display_menu()
        user_choice = input("What would you like to do?")

    return user_choice


# After the user picks one of the two options, prompt them to enter
# a string. All user input should be converted to lowercase.
def main():
    choice = receive_choice()
    while choice != '3':
        source_str = input("Enter the source string: ").lower()
        if choice == '1':
            compressor(source_str)
        else:
            decompressor(source_str)
        choice = receive_choice()
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
