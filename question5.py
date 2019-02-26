# Question 5

def name_facts(firstname):
    # calculate length of name
    length = len(firstname)
    # convert string to all lowercase
    name = str.lower(firstname)
    # if the first letter in the sequence is a then return the appropriate
    # string
    if name[0] == "a":
        starts= "does start with the letter A"
    else:
        starts= "does not start with the letter A"
    # This counts the number of z's and x's in the string

    # sets the count at zero
    x = 0
    for letter in name:
        if letter == "z" or letter == "x":
            x = x + 1

    # If the statement does or does not find a z or x, it will change the
    # contains variable to the proper string
        if x != 0:
            contains = "does contain a Z or X"
        else:
            contains = "does not contain a Z or X"
    # returns a string with all the assigned variables to their proper spot
    return "Your name is %d letters long, %s, and %s" % (length, starts, contains)

first_name = input("First name? ")
name_facts(first_name)
