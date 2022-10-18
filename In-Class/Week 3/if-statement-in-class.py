# NAME: Omar Salah-Eddine
# ID: 5970678517
# DATE: 2022/09/15
# DESCRIPTION: Just the in class assignment I missed

def earlier_name(name1: str, name2: str) -> str:
    """Return the name, name1 or name2, that comes first alphabetically.

    >>> earlier_name('Jen', 'Paul')
    'Jen'
    >>> earlier_name('Colin', 'Colin')
    'Colin'
    """
    # TODO
    return name1 if name1 < name2 else name2


def ticket_price(age: int) -> float:
    """Return the ticket price for a person who is age years old.
    Seniors 65 and over pay 4.75, kids 12 and under pay 4.25 and
    everyone else pays 7.50.

    Precondition: age > 0
    
    >>> ticket_price(7)
    4.25
    >>> ticket_price(21)
    7.5
    >>> ticket_price(101)
    4.75
    """
    # TODO
    if age < 12:
        return 4.25
    elif age >=65:
        return 4.75
    else:
        return 7.50




def format_name(first: str, last: str) -> str:
    """Return the first and last names as a single string, in the form:
    last, first
    Mononymous persons (those with no last name) should have their name
    returned without a comma.

    >>> format_name('Cherilyn', 'Sarkisian')
    'Sarkisian, Cherilyn'
    >>> format_name('Cher', '')
    'Cher'
    """
    # TODO
    return f"{last}, {first}"


def main():
    # TODO
    print(earlier_name("A", "B"))
    print(ticket_price(65))
    print(format_name("B", "A"))


if __name__ == "__main__":
    main()
        
