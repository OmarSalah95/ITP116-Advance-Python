class BankAccount():
    # This will initialize our new instance of a bank acocunt
    #   so we define the data fields based on the input given in instantiation 
    def __init__(self, name, initial_balance):
        # Just assigning the recieved arguments to the corresponding fields of their new bank account
        self.accountHolder = name
        self.balance = initial_balance
    
    # Allows users to deposit money in a given ammount, and updats their account balance accordingly
    def deposit(self, ammount):
        # adds the ammount recieved as an argument to the account balance
        self.balance += ammount
    # Allows users to withdrawl money in a given ammount, and updats their account balance accordingly
    def withdrawl(self, ammount):
        # subtracts the ammount recieved as an argument from the account balance
        self.balance -= ammount
    # Overwrites how this object is stringifies. Python is actually an OOP language in that everything
    #   is an object. i.e. When it comes to the interpreter and language itself all data types like 
    #   booleans, strings, integers, doubles, and really everything else is actually defined as an object
    #   and this is why we can call all sorts of different methods(functions already attached to an object)
    #   or even access some data fields of that object with dot notation. In any case, every object has a 
    #   __str__ method attached somewhere way way way up its ancesstry which is overwritten down the lineage
    #   and this function effectively converts this object into a string in whatever method the last child to
    #   defined. For most objects that are self defined, that means it will just spit out the name of the object
    #   path(What function called it, what type of object it is, and where it is as a ram adress). Instead we will
    #   overwrite it to do what we want it to do for the BankAccount class which is itself creating objects, so we
    #   simply want it to return a string of the relevant account information nicely and thats what we do
    def __str__(self):
        return f"Account Holder: {self.accountHolder}\nBalance: {self.balance}"
    
def main():
    # Create a new instance of BankAccount in the name of john starting with 100$
    ba1 = BankAccount("John", 100)
    # Deposit 400 into Johns account giving him 500%
    ba1.deposit(400)
    # print the stringified version __str__ that we re-defined for the johns account
    print(ba1)
    # Create a new instance of BankAccount for Codi starting with 300$
    ba2 = BankAccount("Codi", 300)
    # Deposit 600$ into Codis account giving him 900$
    ba2.deposit(600)
    # Again print Codis account information
    print(ba2)

# Application execution point.
if __name__ == "__main__":
    main()