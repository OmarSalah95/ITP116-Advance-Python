# NAME: Omar Salah-Eddine
# ID: 5970678517
# DATE: 2022/11/3
# DESCRIPTION: Another in class assignment, this time on file IO again with exception handling which I already did last time lol
# and dictionaries which i recommended, but oh well again LOL I hate these descriptions as you can tell.  
from typing import IO, Dict
from pyparsing import dict_of


def open_file() -> IO:
    file_pointer = None
    # Keep running this loop until we successfully get a good input file that exists and canbe opened then return that pointed
    # in memory so we can use it to load the data into a dictionalry we can use later
    while file_pointer is None:
        try:
            # grab the name of the file from the user
            in_filename = input("Enter the name of the input file: ")
            # try to open it in read mode
            # If this works file pointer will no longer be a null pointer and thus we exit the loop
            file_pointer = open(in_filename, "r")
        except IOError: # Print out an error if one occurs in trying to open the file, and repeat trying
            print(IOError)  
    # Return the pointer we got
    return file_pointer


# returns a dictionary, where keys the word
# are mapped to the numbers
def read_file(input_file_pointer: IO) -> Dict[str, int]:
    # Initialize and empty dictionary to store names as keys and ints as values
    content = {}
    # Go through everyline of the input file, 
    for line in input_file_pointer:
        # Strip the trailing new line character and separate into an array using space as a delimiter. 
        word_and_num = line.strip().split(" ")
        # This is just parsing useful data and storing it so we can use it later.
        content[word_and_num[0]] = int(word_and_num[1])

    # TODO: close the file
    input_file_pointer.close()
    # Return the data dictionary we can use
    return content


def write_file(dict_of_words: Dict[str, int]) -> None:
    # No need to handle exceptions since write will legit create "touch" for my linux friends a new file in the working directory
    # So we grab a file name and make a new file. I would be extra and add the extension like before but meh
    output_filename = input("Enter the name of the output file: ")
    output_file = open(output_filename, "w")
    # TODO: Use a loop to read informaiton from the dictionary and write tehm to the output file.
    # Separate key and value pairs in the dictionary using items to iterate over
    for name, mult in dict_of_words.items():
        # Create take each dictionary entry and multiply the key name + a new line char times the multiple which is the value in the dict
        output_file.write((name+"\n")*mult)

    # TODO: Close output file.
    output_file.close()
    print(output_filename + " has been created.")


# No change is needed in main. Just add comments.
def main():
    # Print welcome message
    print("Welcome to the File Expansion program.")
    # run the open file protocol which grabs a input file name from the user
    input_file_pointer = open_file()
    # Load and parse the content from the file we just opened and close it after
    file_contents = read_file(input_file_pointer)
    # Call the write file protocol which grabs a output file name and then writes all the modified data to that file.
    write_file(file_contents)

# Application execution point.
if __name__ == "__main__":
    main()
