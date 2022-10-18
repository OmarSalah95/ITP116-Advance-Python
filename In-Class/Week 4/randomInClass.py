def runMyName(multiple = 1):
    name = input("What would you like me to call you master?") + "\n" #*4 (another way)
    
    name *= multiple
    # name *= 4 # Another way
    
    # for i in range(multiple): # Another way
    #     print(name)

    print(name)

runMyName(5)