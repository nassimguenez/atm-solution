
MONEY_PIECES = [200, 100, 50, 20, 10, 5, 1]
CURRENCY = 'DZD'
WITHDRAW = 11

def transorform_to_pieces():

    # Initialse Variables:
    to_transforme = WITHDRAW # The amount to be transformed
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

print transform_to_pieces();
