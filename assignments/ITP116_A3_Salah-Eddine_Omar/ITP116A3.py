# TODO Provide comments for *ALL* lines, including the already provided ones.
# TODO Type your comments above the lines.
# TODO Replace all "pass" with proper code.
# NAME: Omar Salah-Eddine
# ID: 5970678517
# DATE: 2022/11/16
# DESCRIPTION: Simple script that allows users to input a network from a txt file, recreate the network, find friends with similarities,
# and recommend those similar friends to users. 


from Graph import *
from typing import IO, Tuple, List
# TODO
PROGRAMMER = "Add your name here"
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
class Member:
    def __init__(self, member_id: int,
                first_name: str,
                last_name: str,
                email: str,
                country: str):
        
        self.id = member_id
        self.firstName = first_name
        self.lastName = last_name
        self.email = email
        self.nationality = country
        self.connections = []

    def add_friend(self, friend_id) -> None:
        self.connections.append(friend_id) # if friend_id not in self.connections else print(f"{friend_id} is already in your friends list!")

    def remove_friend(self, friend_id) -> None:
        self.connections.remove(friend_id) # if friend_id in self.connections else print(f"{friend_id} is not in your friends list!")

    def friend_list(self) -> List[int]:
        return self.connections

    def display_name(self):
        return f"{self.firstName} {self.lastName}"

    def number_of_friends(self) -> int:
        return len(self.connections)

    def show_network(self):
        for connection in self.connections:
            print(connection)


    def __str__(self) -> str:
        return f"Name: {self.firstName} {self.lastName}\nEmail: {self.email}\nFrom: {self.nationality}\nHas {self.number_of_friends()} friends."

def open_file(file_type: str) -> IO: 
    # file_name = input("Enter the " + file_type + " filename:\n")
    # TODO To save time, comment out the above line and uncomment the following section.
    # TODO Do not forget to return it back before submitting.
    if file_type == "profile":
        file_name = "profile_10.csv"
    else:
        file_name = "connection_10.txt"
    file_pointer = None
    while file_pointer is None:
        try:
            file_pointer = open(file_name, "r")
        except IOError:
            print(f"An error occurred while opening the file {file_name}.\n"
                f"Make sure the file path and name are correct \nand that "
                f"the file exist and is readable.")
            file_name = input("Enter the " + file_type + " filename:\n")

    return file_pointer


def create_network(fp: IO) -> List[List[int]]:
    size = int(fp.readline())
    connection = []

    for i in range(size):
        connection.append([])

    line = fp.readline()

    while line is not None and len(line) >= 3:
        split_line = line.strip().split(" ")
        connection[int(split_line[0])].append(int(split_line[1]))
        connection[int(split_line[1])].append(int(split_line[0]))

        line = fp.readline()

    return connection


def num_in_common_between_lists(list1: List, list2: List) -> int:
    degree = 0
    for i in range(len(list1)):
        if list1[i] in list2:
            degree += 1

    return degree


def init_matrix(size: int) -> List[List[int]]:
    matrix = []
    for row in range(size):
        matrix.append([])
        for column in range(size):
            matrix[row].append(0)

    return matrix


def calc_similarity_scores(profile_list: List[Member]) -> List[List[int]]:
    matrix = init_matrix(len(profile_list))

    for i in range(len(profile_list)):
        for j in range(i, len(profile_list)):
            degree = num_in_common_between_lists(profile_list[i].connections,
                                                profile_list[j].connections)
            matrix[i][j] = degree
            matrix[j][i] = degree

    return matrix


def recommend(member_id: int, friend_list: List[int], similarity_list: List[int]) -> int:
    max_similarity_val = -1
    max_similarity_pos = -1

    for i in range(len(similarity_list)):
        if i not in friend_list and i != member_id:
            if max_similarity_val < similarity_list[i]:
                max_similarity_pos = i
                max_similarity_val = similarity_list[i]

    return max_similarity_pos

# Helper to initialization 
def create_members_list(profile_fp: IO) -> List[Member]:
    profiles = []
    profile_fp.readline()
    line = profile_fp.readline()
    profile_list = line.split(',')
    while line is not None and len(profile_list) == 5:
        print("Line" + line)
        ID = int(profile_list[0])
        firstName = profile_list[1].strip()
        lastName = profile_list[2].strip()
        email = profile_list[3].strip()
        nationality = profile_list[4].strip()

        profiles.append(Member(ID, firstName, lastName, email, nationality))
        line = profile_fp.readline()
        profile_list = line.split(',')

    return profiles


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


def receive_verify_member_id(size: int):
    valid = False
    while not valid:
        member_id = input(f"Please enter a member id between 0 and {size-1}:\n")
        if not member_id.isdigit():
            # TODO provide proper message.
            print(f"{member_id} was recieved when we were expecting a digit")
        elif not 0 <= int(member_id) < size:
            # TODO provide proper message.
            print(f"Please enter a member id that is within the range of 0 - {size-1}")
        else:
            valid = True

    return int(member_id)


def add_friend(profile_list: List[Member],
            similarity_matrix: List[List[int]]) -> None:
    size = len(profile_list)
    print("For the first friend: ")
    member1 = receive_verify_member_id(size)
    print("For the second friend: ")
    member2 = receive_verify_member_id(size) # TODO Complete the code
    if member1 == member2:
        print("You need to enter two different ids. Please try again.")
    elif member1 in profile_list[member2].connections:
        # Lol I baked this error handling directly into adding friends method on the member object this is now redundant 
        print("These two members are already friends. Please try again.")
    else:
        profile_list[member1].add_friend(member2)
        profile_list[member2].add_friend(member1)

        print("The connection is added. Please check the graph.")

# Here we are suffering from HORRIBLE specifications again XD why do we need the similarity matrix instead of simply asking for the user we would like to remove?
# Not to mention redundancy, the member object has a remove method built in, there is no reason for us to be doing this like this
# espescially when we have search functionality where we can search the user that wants to delete a friend and just use dot notation
# to remove the friends ID after asking for user input for it. Error handling would be baked in too. 

# The only reason this could need a similarity matrix as a parameter is if the system is by default automaticaly finding and removing 
# members frineds from the list of connections, but even that is entirely illogical since why the hell would any kind of social network
# want to build something in that automatically removes peoples friends from their list.
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


        print("The connection is removed. Please check the graph.")

# This function asks for a country name and list all members from that country.
def search(profile_list: List[Member]) -> None:
    country = input("Please enter the country you would like to search for :").strip()
    filtered = list(filter(lambda member: member.nationality == country, profile_list))
    print()
    for member in filtered:
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
    temp = set()
    for member in profile_list:
        profile_data_str += f"{member.id},{member.firstName},{member.lastName},{member.email}, {member.nationality}\n"
        for connection in member.connections:
            temp.add(f"{member.id} {connection}\n")
    temp = list(temp)
    connection_data_str += "".join(sorted(temp)) 
    print(connection_data_str)



# Do not change
def initialization() -> Tuple[List[Member], List[List[int]], List[List[int]]]:
    profile_fp = open_file("profile") # clear
    profile_list = create_members_list(profile_fp) # Clear

    connection_fp = open_file("connection") # Clear
    network = create_network(connection_fp) # Clear
    print(network)
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
    action = "Continue"
    while action != "Exit":
        action = select_action(profile_list, network, similarity_matrix)

    input("Thanks for using this program.")


if __name__ == "__main__":
    main()
