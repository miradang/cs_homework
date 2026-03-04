''' Name: Miranda Dangerfield
    Assinment: PA2
    Date: 3/3/2026
    
'''
import math

#since prices are hardcoded just shove them in a dict
prices = {"1": "100",
        "2": "119",
        "3": "150",
        "4": "99",
        "5": "199",
        }

#theres gotta be a better way to do this
#maybe nest a dict, look into that

item_name = {"1": "Skittles",
             "2": "Resses",
             "3": "M&M",
             "4": "Chex",
             "5": "Honey",
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
def insert_coinage():
    quit = True
    global total
    global quit_to_main
    print("Please enter:",
        "1.00 for $1 bill",
        "5.00 for $5 bills",
        ".01 for pennies",
        ".05 for nickels",
        ".10 for dimes",
        ".25 for quarters",
        "0 to cancel"
        )
    while quit == True:
        coinage = float(input("Enter in your money: "))
        coinage_quit = round(coinage, 1)
        if coinage_quit == 0:
            quit = False
            quit_to_main = True
            

        else:
            b = coinage_store(coinage)
            total = total + b
            print(f"Your current total is {display_total}.\nEnter 0 to stop deposit")
            return total
        
            
def purchase(item):
    item_price = prices.get(item)
    total = total - item_price
    return total


def purchase_menu():
    global quit_to_main
    print(f"******** Total Money in machine is: {display_total} ********\n",
        "At any point if you wish to cancel operation or go back to last menu, please enter 0.\n",
        "Thank you!:",
        "If you would like to purchase:\n",
        "Skittles type '1', (Price = $1.00)\n",
        "Resse's type '2', (Price = $1.19)\n",
        "M&M's type '3', (Price = $1.50)\n",
        "Chex Mix type '4', (Price = $0.99)\n",
        "Honey Bun type '5'. (Price = $1.99)\n")
    item_entry = input("Your selection is: ")
    if item_entry == 0:
        quit_to_main = True 
    else:
        purchase(item_entry)
        print(total)


def main_menu():
    print("*********\n"
    "Welcome to this Vending Machine!\n",
    "*********\n\n",
    "If you would like to make a selection,\n",
    "please insert the appropriate currency into the machine.\n",
    )

def total_update(number):
    if number == 0:
        return "$0.0"
    
    #calc the power of 10 needed
    #gets exponent of first digita
    exponent = math.floor(math.log10(abs(number)))
    #factor to is 10 to the exponent
    factor = 10 ** exponent
    u_d_total = number // factor
    #returns with only two decimals trailing
    return (u_d_total:.2f)



#global vars

total = 0
display_total = 0
quit_to_main = False

#main programm loop
mainloop = True
while mainloop == True:
    main_menu()
    while quit_to_main == False:
        insert_coinage()
        print(total)
        purchase_menu()


'''
to do:
fix display total to show decimal points
complete purchase

write change function

'''


