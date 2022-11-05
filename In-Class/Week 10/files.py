# NAME: Omar Salah-Eddine
# ID: 5970678517
# DATE: 2022/10/27
# DESCRIPTION: Another in class assignment, this time on file IO.  

# Simple function to prompt users for a file. I misunderstood the header at first. I though the file type was refering to the 
# file extension like .py, .txt, .jsx, .CSV etc. I didnt realize it was really just to add logic to display whether the we are takin
# input or ouput files. 
def get_filename(file_type: str,file_extension: str) -> str:
    # I added basic exception handling here first we prompt the user for the data
    # we are looking for
    fileName = input(f"Please enter the name of the {file_type} file: ")
    # then we return that string as a file path, I can really do just about anything needed here like changing the pathing to 
    # something that works in multiple OS's in this case we are just double checking we have a file extension attached in the 
    # path specifying the file, if not we simply add it to make sure we have no issues here.
    return input if file_extension in fileName else fileName + file_extension


# this is going to read the file path we just got from the user, and parse the data into a 2D matrix where each row represents
# a name and multiple to be repeated. [<name>, <Multiple>].
def read_file(file_path):
    # We will try to run this block, however if it fails we will display the error. We could also add another loop in here
    # if we wanted to continually prompt the user until they give us something we can work with. 
    try:
        # Initialize the return matrix. Even though this can be done more easily with a dictionary
        dataMatrix = []
        # Pop open the file we are reading from in read mode
        input_file = open(file_path, "r")
        # Iterate over all of the lines in the file
        for line in input_file.readlines():
            # Strip the trailing new lines from each line, then split the elements of the line delimited by spaces
            lineRow = line.strip().split(" ")
            # type cast the multiplier to be an int that we can work with more easily later
            lineRow[1] = int(lineRow[1])
            # Append this line to data matrix that we will return
            dataMatrix.append(lineRow)
        # Simply close the file to prevent memory leaks.
        input_file.close()
        # finally now that we have fully populated our data matrix, we can return it to be used elsewhere
        return dataMatrix
    # Just catches the exception incase trying to open the file does not work or an error is enduces, this will then print that error
    # We could also print out the traceback or one of thousands of other options we can use with exception objects in python.
    except IOError:
        print(IOError)

# Simple function that will just take the data we read in, parse and modify it as needed before writing that to a clean new
# output file.
def write_file(list_of_words, output_filename):
    # Again try except, like before no point leaving notes on this one.
    try:
        # Pop open the output file in write mode, so that we can overide any existing data if the file exists, or create a new one if
        # it does not yet exist.
        output_file = open(output_filename, "w")
        # Here wi will simply go through each line row and complete our midification and manipulation before writing each of those new
        # lines into the output file. 
        for line in list_of_words:
            # To spare more looping iterations and efficiency, what we can do is simply add a newline character to each name in
            # from the input data, then muliply that string by the multiple to get a block of text just repeating the specified name
            # we can then write that to out file
            expanded_line = (line[0] + "\n") * line[1]
            output_file.write(expanded_line)
        # No memory leaks please
        output_file.close()
    except IOError:
        print(IOError) 

# Application execution point.
def main():
    # Prompt the user for the file they would like to read from, and clean up the pathing
    input_file_path = get_filename("input", ".txt")
    # Grabs and stores all the data from the read file
    data = read_file(input_file_path)
    # Prompts the user and creates a file path to the output file.
    output_file_path = get_filename("output",".txt")
    # Takes the data from the input, modifies it, and writes it in its modified form to the file. 
    write_file(data, output_file_path)

# application entry point
if __name__ == "__main__":
    main()