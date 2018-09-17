MONEY_PIECES = [200, 100, 50, 20, 10, 5, 1]

# trasform the withdraw money to pieces
def transform_to_pieces(mrequest):

    # Initialse Variables:
    to_transforme = request # The amount to be transformed
    transformed = [] # A reversed Orderd List of the returned number of  each piece
    rest = 0 # The amount that can't be transformed


    for piece in MONEY_PIECES: # Loop through diffrent money possible pieces

        if to_transforme >= piece: # The amount to transforme must be bigger than the piece
            rest = to_transforme % piece # Calculate the amount that can't be transformed
            to_transforme = to_transforme - rest # Calculate the actual amount to be transformed
            transformed.append(to_transforme / piece) # Do the trasformation
            to_transforme = rest # Get ready to the next transformation
        else:
            transformed.append(0)

    return transformed

# display Function
def display(list_of_monye_pieces):
    print "You have withdrawed the following amount of money: \n"
    i = 0
    while i < 6:
        print list_of_monye_pieces[i], " Piece of ", MONEY_PIECES[i], ".\n"
        i += 1

# The core function
def start_withdraw():
    stop_withdraw = False
    while not stop_withdraw:
        status = raw_input("Do you want to proceed to withdraw (yes/no): ")
        if status == "yes":
            request = input("How much would you like to withdraw? : ")
            if (request >= 10) and (request < 1000):
                display(transform_to_pieces(request))
            else:
                print "withdraw amount must be not less than 10 DZD nor bigger than 1000 DZD"
        else:
            stop_withdraw = True

start_withdraw()
