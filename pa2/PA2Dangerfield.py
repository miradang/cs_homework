''' Name: Miranda Dangerfield
    Assinment: PA2
    Date: 3/3/2026
    
'''





#since prices are hardcoded just shove them in a dict
prices = {"skittles": "1.00",
        "resses": "1.19",
        "m&m": "1.50",
        "chex": "0.99",
        "honey": "1.99",
        }
#quit condition
#quit = True

for VendingMachine:
    def __init__(self):
        self.running = True
        #dict for menu selection
        self.options = {
            '1': (self.main_menu),
            '2': (self.insert_coinage),
            '3': (self.purchase),
        }
    
    #stores coinage why the heck did i write this?
    def coinage_store(coinage):
        coinage = float(coinage)
        total = int()
        money = coinage
        a = coinage_convert(money)
        return a

    #converts from float to int
    def coinage_convert(money):
        intmoney = money
        #money = intmoney
        intmoney = int(round(intmoney, 5) * 100)
        return intmoney

    #insert coins menu
    def insert_coinage(self):
        print("Please enter:\n",
        "1.00 for $1 bill\n",
        "5.00 for $5 bills\n",
        ".01 for pennies\n",
        ".05 for nickels\n",
        ".10 for dimes\n",
        ".25 for quarters\n",
        "0 to cancel\n"
        )
        while quit_1 == True:
            coinage = float(input("Enter in your money: "))
            coinage_quit = round(coinage, 1)
            if coinage_quit == 0:
                quit_1 = False
                #doesnt work yet figure it out 

            else:
                total = 0
                b = coinage_store(coinage)
                total = total + b
                print(f"Your current total is {total}.\nEnter 0 to stop deposit")

    def purchase_menu

    def main_menu(self):
        print("*********\n"
        "Welcome to this Vending Machine!\n",
        "*********\n\n",
        "If you would like to make a selection,\n",
        "please insert the appropriate currency into the machine.\n",
        )

    def main_loop(self):
        while self.running:
            while choice == 0
                self.main_menu()
                choice = choice + 1
            self.insert_coinage()

            

 
#main loop
#throw this in a class dude
#while quit == True:
#    print("*********\n"
#        "Welcome to this Vending Machine!\n"
#        "*********\n\n"
#        "If you would like to make a selection,\n"
#        "please insert the appropriate currency into the machine.\n" \
#        "Please enter:\n"
#        "1.00 for $1 bill\n"
#        "5.00 for $5 bills\n"
#        ".01 for pennies\n"
#        ".05 for nickels\n"
#        ".10 for dimes\n"
#        ".25 for quarters\n"
#        "0 to cancel\n")
    
    #coin input loop
#    coinage = ""
#    quit_1 = True

#    while quit_1 == True:
#        coinage = float(input("Enter in your money: "))
#        coinage_quit = round(coinage, 1)
#        if coinage_quit == 0:
#            quit_1 = False
            #doesnt work yet figure it out 

#        else:
#            total = 0
#            b = coinage_store(coinage)
#            total = total + b
#            print(f"Your current total is {total}.\nEnter 0 to stop deposit")
            


#print(f"********* Total Money in machine is: {total} ********"
          "\tAt any point if you wish to cancel operation or go back to last menu, please enter 0.",
           "\tThank you!:",
           "If you would like to purchase:",
           "Product A type '1', (Price = $1.00)",
           "Product B type '2', (Price = $1.25)",
           "Product C type '3', (Price = $1.50)",
           "Product D type '4', (Price = $1.75)",
           "Product E type '5'. (Price = $2.00)",
           "Your entry is: ")




 




    #write coinage to dollars quarters nickets dimes pennies





    
#def float_to_money(money):

#5.36 






