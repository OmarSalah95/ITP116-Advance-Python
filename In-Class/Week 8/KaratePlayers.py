# NAME: Omar Salah
# ID: 5970678517
# DATE: 2022-10-10
# DESCRIPTION:In class assignments in to show all states where 2 players can be on a 1D board of size n with atleast 1 open
#   one open space on either side

def getAllValidStates(n):
    # More simple exception handling. You have no options for valid states with a board of anyting less than 5
    if n < 5:
        return "_"*n

    floor = list("_"*n)
    possibleStates = []
    for p1 in range(1, n): # Starts at 1 since we can not stand on the ends of the floor
        for p2 in range(p1+2, n-1): # Starts 2 spaces over to account for the 1 space gap between players, and ends one short of the
            #   End again to account for not being able to step on the ends

            # Then simply assign the positions on the floor to the playrs
            floor[p1], floor[p2] = "&", "&"
            # Join it into one pretty string with a " " as the delimiter to keep the prints looking clean and legible and 
            # append it to the possible states list
            possibleStates.append(" ".join(floor))
            # Finally reset the original floor list so that we can repeat the cycle clearing the states
            floor = list("_"*n)
    # Then just return this list of state possibilities and bob is your uncle.
    return possibleStates

# Simple helper function to pretty print matrixes
def prettyPrintArray(array):
    print()
    for row, val in enumerate(array):
        print("%3d : %s" % (row, val))


def main():
    prettyPrintArray(getAllValidStates(10))


if __name__ == "__main__":
    main()