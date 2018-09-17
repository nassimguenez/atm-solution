MONEY_PIECES = [200, 100, 50, 20, 10, 5, 1]
MINIMUM_BALANCE = 10

# trasform the withdraw money to pieces
def transform_to_pieces(mrequest):

    # Initialse Variables:
    to_transforme = mrequest # The amount to be transformed
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
def withdraw(mlist_with_each_monye_piece_number):
    i = 0
    while i < len(mlist_with_each_monye_piece_number):
        while mlist_with_each_monye_piece_number[i] > 0:
                print("Give -> %3i DZD" %(MONEY_PIECES[i]))
                mlist_with_each_monye_piece_number[i]-=1
        i+=1

# The core function
def start_withdraw():
    stop_withdraw = False
    balance = 1000
    while not stop_withdraw:
        status = raw_input("Do you want to proceed to withdraw (yes/no): ")
        if status == "yes":
            request = input("How much would you like to withdraw? : ")
            if (request >= 10) and (request < balance):
                withdraw(transform_to_pieces(request))
            else:
                print "withdraw amount must be not less than", MINIMUM_BALANCE, " DZD nor bigger than ", balance, " DZD"
        else:
            stop_withdraw = True

start_withdraw()
