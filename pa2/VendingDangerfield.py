''' Name: Miranda Dangerfield
    Assinment: PA2
    Date: 3/3/2026
    
'''
import math

#just a nested dict for products prices and such
products = {
    '1': {
        'name': 'Skittles',
        'int_price': 100,
        'float_price': 1.00,
    },

    '2': {
        'name': 'Resses',
        'int_price': 119,
        'float_price': 1.19,
    },

    '3': {
        'name': 'M&M',
        'int_price': 150,
        'float_price': 1.50,
    },

    '4': {
        'name': 'Chex',
        'int_price': 99,
        'float_price': 0.99,
    },
    '5': {
        'name': 'Honey Bun',
        'int_price': 199,
        'float_price': 1.99,
    },
}




#converts from float to int
def coinage_convert(money):
    intmoney = int(round(money, 5) * 100)
    return intmoney


#insert coins menu
def insert_coinage():
    global display_total
    global int_total
    global icq
    #grabs global totals

    icq = True
    #why is this here? does this need to be a loop?
    print("Please enter:",
        "1.00 for $1 bill\n",
        "5.00 for $5 bills\n",
        ".01 for pennies\n",
        ".05 for nickels\n",
        ".10 for dimes\n",
        ".25 for quarters\n",
        "0 to cancel"
        )
    while icq == True:
        float_coinage = float(input("Enter in your money: "))
        #rounds coinage to 1 digit to see if its zero for quit condition
        #check to see if i need to return a quit value
        coinage_quit = round(float_coinage, 1)
        int_coinage = coinage_convert(float_coinage)

        if coinage_quit == 0:
            quit_menu()
            return
            #quit condition

        else:
            total_add(int_coinage, float_coinage)
            print(f"Your current total is {float_total:.2f}.\nEnter 0 to stop deposit")
            #calls the function that adds to the total
            #legacy from when i had a total_add and total_sell
         
        
            
def purchase(item):
    #purchase function
    global int_total
    global float_total
    #grabs global totals

    name = products.get(str(item), {}).get("name")
    item_price = products.get(str(item), {}).get("int_price")
    disp_price = products.get(str(item), {}).get("float_price")
    #gets prices for selected item

    if int_total >= item_price:
        #checks to see if you acutally have enough money
        int_total = int_total - item_price
        float_total = float_total - disp_price
        #subtracts price from total
    else:
        print("\nYou dont have enough money\n")
        return
    #subtracts prices from global prices
    #need to check float to make sure it doesnt get to in accurate
    #might need to actaully figure out how to convert int to float well
    print(f"**** This {name} costs {disp_price:.2f} ****")

def change():
    global int_total
    working_total = int_total

    #167 as example
    cents = working_total
    quarters = cents // 25
    #6 quarters
    cents %= 25
    #remainder 17
    dimes =  cents // 10
    #1 dimes
    cents %= 10
    #remainder 7
    nickels = cents // 5
    #1 nickel
    cents %= 5
    #remainder 2

    print(f"****You have ${float_total:.2f} left in the machine ****\n",
    "Your change is:\n",
    f"{quarters} Quarters\n",
    f"{dimes} Dimes\n",
    f"{nickels} Nickels\n",
    f"{cents} Pennies\n",
    )
   


def purchase_menu():
    #purchase menu

    #need to write better quit conditions this is wack

    print(f"******** Total Money in machine is: {float_total:.2f} ********\n",
        "At any point if you wish to cancel operation or go back to last menu, please enter 0.\n",
        "Thank you!:",
        "If you would like to purchase:\n",
        "Skittles type '1', (Price = $1.00)\n",
        "Resse's type '2', (Price = $1.19)\n",
        "M&M's type '3', (Price = $1.50)\n",
        "Chex Mix type '4', (Price = $0.99)\n",
        "Honey Bun type '5'. (Price = $1.99)\n")
    item_entry = int(input("Your selection is: "))
    while True:
        if item_entry == 0:
            quit_menu()
        elif item_entry not in range(1,6):
            print("Invalid entry")
            item_entry = int(input("Your selection is: "))
        else:
            purchase(item_entry)
            change()
            purchase_menu()

        
def loop_quit():
    global mainloop
    global pmq
    global icq
    global loopone
    #was having trouble ending the main loop so im turning every quit condition false at once
    #it is the middle of the night have mercy
    mainloop, pmq, icq, loopone = False, False, False, 1
    raise SystemExit


def main_menu():
    #main menu for vending machines
    print("*********\n"
    "Welcome to this Vending Machine!\n",
    "*********\n\n",
    "Enter 0 ant anytime to quit\n",
    "If you would like to make a selection,\n",
    "please insert the appropriate currency into the machine.\n",
    )
    #with the current state of the loop this can repeat infinitly


def total_add(int_coinage, float_coinage):
    
    global int_total
    global float_total

    int_total = int_coinage + int_total
    float_total = float_coinage + float_total

    #print(f"totaladd {int_total}")
    #display_total = f"${int_total:.2f}"
    

def total_sub(int_coinage, float_coinage):
    #do i still need this, i dont think it gets called anywhere
    global int_total
    global float_total

    int_total = int_total - int_coinage
    float_total = float_total - float_coinage

    print(f"totalsub {int_total}")
    #display_total = f"${int_total:.2f}"


def quit_menu():
    global mainloop

    print("Enter 0 to quit\n",
          "Enter 1 to insert coinage\n",
          "Enter 2 to purchase products\n",
          )
    option = int(input("Enter a selection here: "))
    if option == 0:
        loop_quit()
        return

    elif option not in range(0, 3):
        option = int(input("Invalid selection. Enter a selection here: ")) 
            
    elif option == 1:
        insert_coinage()

    elif option == 2:
        purchase_menu()

    else:
        print("Something broke in quit menu")
        option = int(input("Enter a selection here: "))



#####global vars


int_total = 0
#total in int
float_total = 0
#total in float
display_total = ""
#i dont think this is used
loopone = 0
#need to fix all the quit conditions to be standardized
#####End of global vars

######main programm loop#########
mainloop = True

while mainloop == True:
    while loopone == 0:
        main_menu()
        loopone = 1
    insert_coinage()
    purchase_menu()
    quit_menu()
    

'''
to do:
fix display int_total to show decimal points x
make a display int_total for amount left in machine x
fix the decmials on display totals and item prices x
complete purchase x

write change function x

write options def for loop x

fix loop so you can bounce between main menu, insert, purchase, quit x

will need a quit def x

'''


