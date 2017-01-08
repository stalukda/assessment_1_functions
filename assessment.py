"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(25, "CA")
    27.0

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0)
    150

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

def match_hometowns(town_name):
    """Evaluate if town_name input is my home-town. 

    Takes a town name as a string and evaluates to
    `True` if it is your hometown, and `False` otherwise.

    """

    if town_name == "Dhaka":
        return True 
    else:
        return False 

# is_hometown("Dhaka")
# is_hometown("London")


#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

def join_names(first_name, last_name):
    """ Join the input first and last names together into one string. 

        Takes a first and last name as arguments and
        returns the concatenation of the two names in one string.
    """

    full_name = first_name + " " + last_name
    return full_name

# join_names("Sumaiya", "Talukdar")
# join_names("Albert", "Einstein")

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.

def match_backgrounds(home_town, first_name, last_name):
    """ Call previous is_hometown function and print out message based on common or divergent backgrounds

        Taking a home town, a first name, and a last name as arguments, call 
        is_hometown and match_backgrounds functions and print 
        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
        here', where are you from?" depending on commanility or divergent backgrounds 
    
    """
    name = join_names(first_name, last_name)
    home_town = match_hometowns(home_town)

    if home_town == True:
        print "Hi, {}, we're from the same place".format(name)
    else:
        user_town = raw_input("Hi, {}, where are you from?\n".format(name))
        print "I hear it's lovely in {}! Goodbye!".format(user_town)
    # is_hometown(home-town)    

# match_backgrounds("London", "Albert", "Einstein")

###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."

def is_berry(fruit):
    """Determines if fruit is a berry"""
    if fruit == "strawberry" or fruit == "cherry" or fruit == "blackberry":
        return True
    else:
        return False


# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.

def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""

    berry = is_berry(fruit)

    if berry == True:
        return 0
    else:
        return 5 

# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""

    lst.append(num)
    print lst
    

append_to_list([3, 5, 7], 2)


# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.

def calculate_price(base_price, state, tax = .05):

    """Calculate what to pay for an item based on state, including taxes and other fees 

    Calculate the full price of an item by state including base price + taxes + fees. 
    The default taxrate is 5% and fees is none. 
    """

    item_total = base_price + (base_price * tax)

    if state == "CA":
        item_total = item_total + (item_total * .03)
        item_total
    elif state == "PA":
        item_total = item_total + 2
    elif state == "MA":
        if base_price < 100:
            item_total = item_total + 1 
        else:
            item_total = item_total + 3
    else:
        print item_total
        return 

    print round(item_total, 1)


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.

def return_list(lst, *args):

    """Append an undetermined number of items to a list. 

    Take in a list and any number of additional arguments, append them to the list, 
    and return the entire list. 
    """
    lst.append(args)
    return lst 

return_list([3, 5, 7], 2, 5, "barbara")

# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

def accept_word(word):

    """ Print out a string of 3x the inputted word. 

    """ 
    def multiple(word):
        extended_word = word * 3 
        print (word, extended_word)
        return word, extended_word
    multiple(word)

accept_word("Balloonicorn")

###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
