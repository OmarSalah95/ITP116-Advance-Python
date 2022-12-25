# NAME: Omar Salah-Eddine
# ID: 5970678517
# DATE: 2022/11/16
# DESCRIPTION: Simple script that allows users to input a network from a txt file, recreate the network, find friends with similarities,
# and recommend those similar friends to users. 


from Graph import *
from typing import IO, Tuple, List
# TODO Defining a bunch of global variables.
PROGRAMMER = "Omar Salah"
MEMBER_INFO = "1"
NUM_OF_FRIENDS = "2"
LIST_OF_FRIENDS = "3"
RECOMMEND = "4"
SEARCH = "5"
ADD_FRIEND = "6"
REMOVE_FRIEND = "7"
SHOW_GRAPH = "8"
SAVE = "9"
LINE = "\n*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*_*-*\n"


# TODO Complete the class.
class Member: # Define a member class thatwill store our data and make methods available
    def __init__(self, member_id: int,
                first_name: str,
                last_name: str,
                email: str,
                country: str):
        # Simple variable definitions here upon instantiation of the member class we do a bunch of assignments
        self.id = member_id
        self.firstName = first_name
        self.lastName = last_name
        self.email = email
        self.nationality = country
        self.connections = []
    # Since this will function as a helper method, we will simply use it to add ID's to a friends user list, I commented out the additional error handling
    def add_friend(self, friend_id) -> None:
        self.connections.append(friend_id) # if friend_id not in self.connections else print(f"{friend_id} is already in your friends list!")
    # Does the opposite of add in basically the same exact way just reversed
    def remove_friend(self, friend_id) -> None:
        self.connections.remove(friend_id) # if friend_id in self.connections else print(f"{friend_id} is not in your friends list!")
    # helper method to dump the connections to be used when we could use it. 
    def friend_list(self) -> List[int]:
        return self.connections
    # Getters and setters here, just another helper to display a members full name
    def display_name(self):
        return f"{self.firstName} {self.lastName}"
    # returns the number of friends a member has
    def number_of_friends(self) -> int:
        return len(self.connections)
    # This is just an additional helper function I used to help during testing to confirm adding and subtracting
    def show_network(self):
        for connection in self.connections:
            print(connection)
    # Overwrites the to string method for the member object to display the pertinant data.
    def __str__(self) -> str:
        return f"Name: {self.firstName} {self.lastName}\nEmail: {self.email}\nFrom: {self.nationality}\nHas {self.number_of_friends()} friends."

# Just opens a file specified by a user so that we can pass the pointer around as needed when loading data. Particularly since we are 
# using 2 separate files to open data, this is really just a utility
def open_file(file_type: str) -> IO: 
    # First thing is first pull the file name we want to open from the user
    file_name = input("Enter the " + file_type + " filename:\n")
    # if file_type == "profile":
    #     file_name = "profile_10.csv"
    # else:
    #     file_name = "connection_10.txt"

    # This gives us our continually false condition which will ensure we do not exit the loop until we have a usable
    # open file, otherwise we will continue to ask the user for inputs until we can successfully open the file we are 
    # loading data from 
    file_pointer = None
    while file_pointer is None:
        # Try catch block, very simple. Try to open the file, if it fails display a bunch of messages then grab another input from
        # the user again to try again as the loop continues
        try:
            file_pointer = open(file_name, "r")
        except IOError:
            print(f"An error occurred while opening the file {file_name}.\n"
                f"Make sure the file path and name are correct \nand that "
                f"the file exist and is readable.")
            file_name = input("Enter the " + file_type + " filename:\n")
    # if we made it this far, then we definitely have a good file pointer we can pass out to wherever it is needed. 
    return file_pointer

# This basically creates our network by mapping the connections in the connection files, to their respective users by ID adding 
# the friend IDs to the list of connections each user has
def create_network(fp: IO) -> List[List[int]]:
    # strip the first line which is just giving us the length of the network 
    size = int(fp.readline())
    # initiates an empty array of connections that can be stored in the member object
    connection = []
    # Creates a good matrix, with 1 row for each user representing the connections.
    for i in range(size):
        connection.append([])
    # Preemptively grab the next line in preparation for a while loop so we are not working with bad data, and can use it
    # in our condition
    line = fp.readline()
    # Here we are going to simply parse the data, and in the new matrix we above where we generate our list of connections 
    # that will be returned
    while line is not None and len(line) >= 3:
        # Parse the data chopping the line at each space, and stripping any escape sequences so we can type case, and append the data
        # to its relative location in the network
        split_line = line.strip().split(" ")
        connection[int(split_line[0])].append(int(split_line[1]))
        connection[int(split_line[1])].append(int(split_line[0]))
        # move onto the next line before we repeat our loop
        line = fp.readline()
    # Do you seriously need this many comments? It just returns the thing here
    return connection

# Calculates number of friends in common between two list of friends. Basically finds all the friends 2 users share
def num_in_common_between_lists(list1: List, list2: List) -> int:
    # Initialize a counter to show how many friends users have in common
    degree = 0
    # Go through one list, comparing if each item in list one is in list 2 if it is, we increment our degree counter indicating
    # an additoinal friend in common and move on
    for i in range(len(list1)):
        if list1[i] in list2:
            degree += 1
    # return the number of frieds these 2 lists have in common
    return degree

# Creates an empty nxn matrix
def init_matrix(size: int) -> List[List[int]]:
    # Initialize
    matrix = []
    # Creates a new row to match the size we are given size = n
    for row in range(size):
        # Adds a new empty row
        matrix.append([])
        # Nested loop iterates to the same n filling each column in the matrix with a 0
        for column in range(size):
            # adds a zero in each column
            matrix[row].append(0)
    # Return the thing
    return matrix


def calc_similarity_scores(profile_list: List[Member]) -> List[List[int]]:
    # Generates an empty matrix using the function above before we populate the data
    matrix = init_matrix(len(profile_list))
    # Nested loops for more row and column action except this time we are calculating the degree of similarity each user has with
    # the other users, then plugging that into the matrix 
    for i in range(len(profile_list)):
        for j in range(i, len(profile_list)):
            # Here we are doing the thing, calling num in common so that we can get that degreee
            degree = num_in_common_between_lists(profile_list[i].connections,
                                                profile_list[j].connections)
            # This handles double assignment since our similarity matrix should always be symetric
            # about the main diagonal.Another decent option here would be to implement a binary filling
            # method so that we can get O(n/2) and reap the benefits of the symettry as opposed the O(n) solution this is
            matrix[i][j] = degree
            matrix[j][i] = degree
    # return the thing
    return matrix

# This method reccomends a friend to add given a user ID. This method will check the similarity matrix finding which other user
# has the highest degree of friends in common with the given user, checks that they are not already friends, and then recommends that person
def recommend(member_id: int, friend_list: List[int], similarity_list: List[int]) -> int:
    # assign low defaults so we dont accidently trigger our conditions. The goal here is to not reccomend the user add themselves,
    # or someone that is already on their friends list. 
    max_similarity_val = -1
    max_similarity_pos = -1

    for i in range(len(similarity_list)):
        # first check to make sure the user is not in our friend list and is not the same as the member ID we recieved as an argument
        if i not in friend_list and i != member_id:
            if max_similarity_val < similarity_list[i]:
                # Set the new id of the member that has the current highest similarity score
                max_similarity_pos = i
                # Set the highest similarity score we have seen thus far.
                max_similarity_val = similarity_list[i]
                
    # return the thing
    return max_similarity_pos

# Helper to initialization 
def create_members_list(profile_fp: IO) -> List[Member]:
    # Create an empty list
    profiles = []
    # Read past the header of the CSV file so we can get to our data
    profile_fp.readline()
    # Strip one full line of user data from the csv file
    #   This will be in the shape of 
    #    id,first_name,last_name,email,country
    line = profile_fp.readline()
    # Take the line of data, and split it at each , turning it into a list of substrings minus the delimeter
    profile_list = line.split(',')
    # WHile there are still lines that we can read from the file and all the necessary data is present
    while line is not None and len(profile_list) == 5: 
        # split all the data from the line and clean it so we can use it to instantiate a new member object to add to our
        # profiles list.
        ID = int(profile_list[0])
        firstName = profile_list[1].strip()
        lastName = profile_list[2].strip()
        email = profile_list[3].strip()
        nationality = profile_list[4].strip()
        # This would be much prettier just using the spread operator on that data from the line
        profiles.append(Member(ID, firstName, lastName, email, nationality))
        # Rinse and repeat condition moving us to the next line so we can run the while loop condition and repeat
        line = profile_fp.readline()
        profile_list = line.split(',')
    # Return the thing 
    return profiles

# Display menu, honestly python is syntactic enough that I really hope I do not need to commepnt on this other than it diplays a menu
# and of available options to the user and recieves and input which we immediately return as the user selected option later in the 
# REPL
def display_menu():
    print("\nPlease select one of the following options.\n")
    print(MEMBER_INFO + ". Show a member's information \n" +
        NUM_OF_FRIENDS + ". Show a member's number of friends\n" +
        LIST_OF_FRIENDS + ". Show a member's list of friends \n" +
        RECOMMEND + ". Show a friend for a memeber \n" +
        SEARCH + ". Search for a Member\n" +
        ADD_FRIEND + ". Add a friend\n" +
        REMOVE_FRIEND + ". Remove a friend\n" +
        SHOW_GRAPH + ". Show a graph of member connections\n" +
        SAVE + ". Save data" 
        )

    return input("Press any other key to exit.\n")

# Grabs a user ID from the user and ensures it is validated before sending this input to other locations in the code
def receive_verify_member_id(size: int):
    # Exit condition initialization before while lloop
    valid = False
    # WHile the input recieved is not valid, we will continue to badger the user until they give us a good input, otherwise they will 
    # be doomed trapped in this loop until the end of time, or until they terminate the process.
    while not valid:
        # Grab a member ID from the user
        member_id = input(f"Please enter a member id between 0 and {size-1}:\n")
        # make sure its a number, if not complain to the user then ask again
        if not member_id.isdigit():
            # TODO provide proper message.
            print(f"{member_id} was recieved when we were expecting a digit")
        # Confirm it is an integer within the range of member ID's used,if not complain to the user about it and ask again
        elif not 0 <= int(member_id) < size:
            # TODO provide proper message.
            print(f"Please enter a member id that is within the range of 0 - {size-1}")
        else:
            # If none of those other tests failed, then the input must be valid so lets exit this loop and return that sucker
            valid = True
    # Type cast our string to an actual integer and return that value so we can use these ID's elsewhere
    return int(member_id)

# This does the adding for the network, asks the user for 2 member ID's so that they can be added as friends
def add_friend(profile_list: List[Member],
            similarity_matrix: List[List[int]]) -> None:
    size = len(profile_list)
    print("For the first friend: ")
    # Grab a verified ID for 1 member
    member1 = receive_verify_member_id(size)
    print("For the second friend: ")
    # do it again for the second member
    member2 = receive_verify_member_id(size) # TODO Complete the code
    # Make sure that these 2 members are unique and are not already friends
    if member1 == member2:
        print("You need to enter two different ids. Please try again.")
    elif member1 in profile_list[member2].connections:
        # Lol I baked this error handling directly into adding friends method on the member object this is now redundant 
        print("These two members are already friends. Please try again.")
    else:
        # If those checks failed, then we will add the friend to each of the respective memebrs before recalculating the similarity
        # matrix now that changes have been made
        profile_list[member1].add_friend(member2)
        profile_list[member2].add_friend(member1)
        similarity_matrix = calc_similarity_scores(profile_list)

        print("The connection is added. Please check the graph.")

# Basically the same as add in reverse, all the comments above are basically the same, just in reverse.
def remove_friend(profile_list: List[Member], similarity_matrix: List[List[int]]) -> None:
    size = len(profile_list)
    print("For the first friend: ")
    member1 = receive_verify_member_id(size)
    print("For the second friend: ")
    member2 = receive_verify_member_id(size) 
    if member1 == member2:
        print("You need to enter two different ids. Please try again.")
    elif member1 not in profile_list[member2].connections:
        print("These two members are not friends friends. Please try again.")
    else:
        profile_list[member1].remove_friend(member2)
        profile_list[member2].remove_friend(member1)
        similarity_matrix = calc_similarity_scores(profile_list)

        print("The connection is removed. Please check the graph.")

# This function asks for a country name and list all members from that country.
def search(profile_list: List[Member]) -> None:
    # Grab the query country from the user
    country = input("Please enter the country you would like to search for :").strip()
    # Filter using a lambda function that will filter the profile list creating a new list of only members
    # whos nationality matches the query country
    filtered = list(filter(lambda member: member.nationality == country, profile_list))
    # buy a line of space for formating
    print()
    # Print each members that matches the search criteria's information to the console with some nice space
    for member in filtered:
        # use that pretty overwritten string method we made for the member class
        print(member, "\n")


# Do not change.
def add_friends_to_profiles(profile_list: List[Member],
                            network: List[List[int]]) -> None:
    for i in range(len(profile_list)):
        profile_list[i].connections = network[i]

#  Fix This first to test
def select_action(profile_list: List[Member],
                network: List[List[int]],
                similarity_matrix: List[List[int]]) -> str:
    response = display_menu()

    print(LINE)
    size = len(profile_list)

    if response in [MEMBER_INFO, NUM_OF_FRIENDS, LIST_OF_FRIENDS, RECOMMEND]:
        member_id = receive_verify_member_id(size) # CleAR
    # Why is this not a switch case? This long cascade is pointless
    if response == MEMBER_INFO:
    # TODO Complete the code
        print(f"{profile_list[member_id]}")
    elif response == NUM_OF_FRIENDS:
        # TODO Complete the code
        print(f"{profile_list[member_id].number_of_friends()}")
    elif response == LIST_OF_FRIENDS:
        # TODO Complete the code
        print(f"{profile_list[member_id].friend_list()}")
    elif response == RECOMMEND:
        # TODO Complete the code
        recommend(member_id, network, similarity_matrix)
    elif response == SEARCH:
        # TODO Complete the code
        search(profile_list)
    elif response == ADD_FRIEND:
        # TODO Complete the code
        add_friend(profile_list, similarity_matrix)
    elif response == REMOVE_FRIEND:
        # TODO Complete the code
        remove_friend(profile_list, similarity_matrix)
    elif response == SHOW_GRAPH:
        tooltip_list = []
        for profile in profile_list:
            tooltip_list.append(profile)
        graph = Graph(PROGRAMMER,
                    [*range(len(profile_list))],
                    tooltip_list, network)
        graph.draw_graph()
        print("Graph is ready. Please check your browser.")
    elif response == SAVE:
        # TODO Complete the code
        save_changes(profile_list)
    else:
        return "Exit"

    print(LINE)

    return "Continue"


def save_changes(profile_list: List[Member]) -> None:
    profile_data_str = "id,first_name,last_name,email,country\n"
    connection_data_str = f"{len(profile_list)}\n"
    for member in profile_list:
        profile_data_str += f"{member.id},{member.firstName},{member.lastName},{member.email}, {member.nationality}\n"
        for connection in member.connections:
            temp = f"{member.id} {connection}"
            if temp[::-1] not in connection_data_str:
                connection_data_str += temp+"\n"


    profileFP = open(f"profile_{len(profile_list)}.csv", "w")
    connectionsFP = open(f"connection_{len(profile_list)}.txt", "w")

    profileFP.write(profile_data_str)
    connectionsFP.write(connection_data_str)

    profileFP.close()
    connectionsFP.close()
    print("Data Saved Successfully")



# Do not change
def initialization() -> Tuple[List[Member], List[List[int]], List[List[int]]]:
    profile_fp = open_file("profile") # clear
    profile_list = create_members_list(profile_fp) # Clear

    connection_fp = open_file("connection") # Clear
    network = create_network(connection_fp) # Clear
    add_friends_to_profiles(profile_list, network) # Clear
    similarity_matrix = calc_similarity_scores(profile_list) # Clear

    profile_fp.close()
    connection_fp.close()

    return profile_list, network, similarity_matrix

#  Do not change.
def main():
    print("Welcome to the network program.")
    print("We need two data files.")
    profile_list, network, similarity_matrix = initialization()
    print("Network Size: ", len(network))
    action = "Continue"
    while action != "Exit":
        action = select_action(profile_list, network, similarity_matrix)

    input("Thanks for using this program.")


if __name__ == "__main__":
    main()
