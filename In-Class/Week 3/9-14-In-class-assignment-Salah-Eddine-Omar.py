import random


def getValidBounds():
    while True:
        lBound = int(input("Enter the lower bound: "))
        uBound = int(input("Enter the upper bound: "))
        if lBound < uBound:
            return [lBound, uBound]
        else:
            print("The upper bound must be larger than the lower bound.")


def getValidGuess(lBound, uBound):
    userInput = None 
    while True:
        userInput = int(input("Guess a number: "))
        if userInput >= lBound and userInput <= uBound:
            return userInput
        else:
            print(f"{userInput} is outside the range of possible values.")


def guess():
    userInput = 0 
    lBound, uBound = getValidBounds()
    num = random.randint(lBound, uBound)
    # print(num) # You can uncomment this line to cheat and test all the conditions are met for passing tests
    print(f"I am thinking of a number between {lBound} and {uBound}") 

    while userInput != num:
        userInput = getValidGuess(lBound,uBound)
        print(f"{userInput} is too low.") if userInput < num else print(f"{userInput} is too high.")
    print("You guessed it!")


def main():
    while True:
        guess()
        if input("Do you want to play again? Enter y for yes.") != "y":
            break
    print("Thank you for playing!")


if __name__ == "__main__":
    main()
