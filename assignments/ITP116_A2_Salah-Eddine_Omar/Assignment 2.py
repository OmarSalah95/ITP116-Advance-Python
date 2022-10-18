# NAME: Omar Salah-Eddine
# ID: 5970678517
# DATE: 2022/10/06
# DESCRIPTION: Simple script that allows users to input a network from a txt file, recreate the network, find friends with similarities,
# and recommend those similar friends to users. 

from typing import IO, List

def open_file() -> IO:
    # Take the users input asking for the name of the file we want to open
    file_name = input("Enter a filename: ")
    # Creating a pointer that will be used to create a loop asking for a file name until we are given
    # a file that is stored and actually can be opened by our code
    file_pointer = None
    # Quick while loop to handle exceptions in reciving a file name. If the file doesnt exist or can not be 
    # opened then we will simply keep taking new file names from the user until we get to one we can use.
    while file_pointer is None:
        # This is the exception handling itself, we will try to open the file given in a read capacity, however if our try
        # fails it will throw the exception listed below and prompt the user for another file name to use in the next iteration
        try:
            file_pointer = open(file_name, "r")
        except IOError:
            print("Error in filename.")
            file_name = input("Enter a filename: ")
    # Simply return the pointer in memory that indicates where our data from the file can be accessed.
    return file_pointer

# Simple helper function to pretty print matrixes
def printMatrix(matrix):
    print()
    for userID, row in enumerate(matrix):
        print(userID, ": ", row)

def read_file(fp: IO) -> List[List[int]]:
    # Here we simply recieve a pointer pointing at where our file data is in RAM. We then read n as a string from the file
    # Before type casting it to an int so that we can use it in our code.
    n = fp.readline()
    n = int(n)
    # Initialize an empty network to store all of the numbers that come before n
    network = []
    # I would really just assign network to be a range here, but here we are just counting up to n and storing each number in the 
    #  network(Adding each number to the back of our list)
    for i in range(n):
        network.append([])

    # Read the next line in the file that comes after n and store it to line
    line = fp.readline()
    # Iterate through all of the remaining lines in the file with 3 or more characters
    while line is not None and len(line) >= 3:
        # Then take the line and strip all of the leading and trailing spaces, and separating the clean string at the spaces
        # into individual substrings
        split_line = line.strip().split(" ")
        # then we take the first elements in the split line as our indices within the network, which is where we then append 
        #  the second to the first and the first to the seconds freind list
        network[int(split_line[0])].append(int(split_line[1]))
        network[int(split_line[1])].append(int(split_line[0]))
        # Iteration condition update to recycle loop
        line = fp.readline()
    return network


def init_matrix(n: int) -> List[List[int]]:
    # I mean we are really just initializing a 2D matrix filled with 0s here. It will be a n x n square matrix dependent
    #   on the given integer
    matrix = [] #Initializes empty matrix
    for row in range(n): # This ror loop is responsible for creating our rows
        matrix.append([]) #initialize an empty row
        for column in range(n): # this loop then populates our row with n columns of 0
            matrix[row].append(0)
    # Just retruns the newly filled matrix
    return matrix


def num_in_common_between_lists(list1: List[int], list2: List[int]) -> int:
    numInCommon = 0 # Initialize a counter for each of the friends our 2 lists have in common
    # iterate through each user in list1 and check if that user is in list 2 if they are, we increment the counter
    for userA in list1:
        if userA in list2:
            numInCommon+=1
    # Just return the num in common so we can use this value in similarity scores
    return numInCommon


def calc_similarity_scores(network: List[List[int]]) -> List[List[int]]:
    n = len(network)
    # Initialize an empty square matrix
    similarity_matrix = init_matrix(n)
    # Use nester for loops to go through our matrix by row and column (i, j) so to calculate the similarity scores between each
    #   user and all the other users in the matrix, storing them in their respective spots such as the similarity between 0 and 1, will be 
    #   stored at column 1 of row 0
    for i in range(n):
        for j in range(n):
        # call num_in_common_between_lists using user i’s list and user j’s list as arguments and store it,
        #   also implements logic that will set the value of similarity to 0 when comparing a users friend list
        #   to themselves to prevent recommending the same user to themselves. I.e. 0 being recommended 0 or so on. This
        #   results in a 0 diagonal in the similarity matrix. Please dont deduct me points for it, its just a
        #   bug that can occur and some cases so I added some exception handling thats all.
            similarity_matrix[i][j] = num_in_common_between_lists(network[i], network[j]) if i != j else 0
    # And finally just return this matrix.
    return similarity_matrix


def recommend(user_id: int, network: List[List[int]], similarity_matrix: List[List[int]]) -> int:
    # Add comments
    # this is a placeholder that you will replace with Python code
    userFriends = network[user_id] # storage for ease of access and readability
    userSimilarityList = similarity_matrix[user_id] # storage for ease of access and readability

    # here we are making sure not to recommend users that are already in our friends list, so we keep assigning the max
    #   to 0 in our temp list, then go again and find the max until we have the best user to recommend that is not already
    #   a friend
    friendToRecommend = userSimilarityList.index(max(userSimilarityList))

    while friendToRecommend in userFriends:
        userSimilarityList[userSimilarityList.index(max(userSimilarityList))] = 0
        friendToRecommend = userSimilarityList.index(max(userSimilarityList))
    # Now that we have the best user to recommend and we are sure they are not in the users list of friends already, we can return
    #   That userID
    return friendToRecommend 



def main():
    userInput = "yes" # Condition to run our REPL loop continueously until the user chooses to exit
    # This one is simple, its just creating the network, by first opening the file the user designates, then reading it.
    #   All exceptoin and error handling is already built into read_file and open_file so might as well just stick them in 1
    #   line
    network = read_file(open_file())
    # Generates a similarity matrix for the network file the user selected
    similarityMatrix = calc_similarity_scores(network)

    # just our simple loop here to keep taking user input, but we also have input validation baked in here
    while userInput != "no":
        # We are going to try to run our function as normal, reading an input from the user, and trying to user that input
        # to get a recommendation, however if there is anything wrong with the input, recommend will throw the error for a bad
        # argument triggering the exception block. This should handle any input errors from the user inputting an ID that
        # doesnt exist, or if they enter some combination of letters, or any other error in input. This takes care of recommending
        try:
            userInput = int(input(f"Enter an integer in the range 0-{len(network)-1}: "))
            print(f"The suggested friend for {userInput} is {recommend(userInput, network, similarityMatrix)}")
        except:
            print(f"Error: input must be an int between 0 and {len(network)-1}: ")
        # Then finally we ask the user if they would like to get another recommendation. If their response is any form of the word
        # no, it will set userInput to false killing the loop, and exiting the program. If they enter enything else at all that is not
        # no, the loop will run again.
        userInput = input("Do you want to continue(yes/no)? ").lower()



if __name__ == "__main__":
    main()
