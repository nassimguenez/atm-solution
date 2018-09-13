
MONEY_PIECES = [200, 100, 50, 20, 10, 5, 1]
CURRENCY = 'DZD'
WITHDRAW = 11

def transorform_to_pieces():

    to_transforme = WITHDRAW
    transformed = []
    rest = 0

    for piece in MONEY_PIECES:

        if to_transforme >= piece:
            rest = to_transforme % piece
            to_transforme = to_transforme - rest
            transformed.append(to_transforme / piece)
            to_transforme = rest
        else:
            transformed.append(0)

    return transformed

print transform_to_pieces();
