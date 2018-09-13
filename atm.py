MONEY_PIECES = [200, 100, 50, 20, 10, 5, 1]

def transform_to_pieces(mwithdraw):

    # Initialse Variables:
    to_transforme = mwithdraw # The amount to be transformed
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

def display(list_of_monye_pieces, CURRENCY):
    print "You have withdrawed the following amount of money: \n"
    i = 0
    while i < 6:
        print list_of_monye_pieces[i], " Piece of ", MONEY_PIECES[i], ".\n"
        i += 1

def start_withdraw():
    CURRENCY = 'DZD'
    withdraw = input("How much would you like to withdraw? : ")
    display(transform_to_pieces(withdraw), CURRENCY)

start_withdraw()
