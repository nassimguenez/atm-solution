class Atm:

    MONEY_PIECES = [200, 100, 50, 20, 10, 5, 1]
    MINIMUM_BALANCE = 10

    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self, mlist_with_each_monye_piece_number):
        status = raw_input("Are Sure You Want To Proceed (yes/no)?: ")

        if status == 'yes':
            i = 0
            while i < len(mlist_with_each_monye_piece_number):
                while mlist_with_each_monye_piece_number[i] > 0:
                        print("Give -> %3i DZD" %(self.MONEY_PIECES[i]))
                        mlist_with_each_monye_piece_number[i]-=1
                i+=1
        else:
            print "Procedure Has Been Aborted! \n"

    def transform_to_pieces(self, request):
        # Initialse Variables:
        to_transforme = request # The amount to be transformed
        transformed = [] # A reversed Orderd List of the returned number of  each piece
        rest = 0 # The amount that can't be transformed

        for piece in self.MONEY_PIECES: # Loop through diffrent money possible pieces

            if to_transforme >= piece: # The amount to transforme must be bigger than the piece
                rest = to_transforme % piece # Calculate the amount that can't be transformed
                to_transforme = to_transforme - rest # Calculate the actual amount to be transformed
                transformed.append(to_transforme / piece) # Do the trasformation
                to_transforme = rest # Get ready to the next transformation
            else:
                transformed.append(0)

        return transformed

    def run(self):
        run = True
        while run:
            print "Welcome To Our Service \n"
            print "What Do You Want To Do? \n"
            status = input(" Press: \n 1: (To Display Your Balance) \n 2: (To Make A Withdraw) \n 3: (To Exit) \n ")

            if status == 1:
                print "\n Your Balance is : ", self.balance, "\n"
            elif status == 2:
                request = input("\n How much would you like to withdraw? : ")
                if (request >= 10) and (request < self.balance):
                    self.withdraw(self.transform_to_pieces(request))
                else:
                    print "\n withdraw amount must be not less than", self.MINIMUM_BALANCE, " DZD nor bigger than ", self.balance, " DZD\n"
            elif status == 3:
                run = False
