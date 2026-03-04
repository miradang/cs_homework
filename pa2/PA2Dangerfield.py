''' Name: Miranda Dangerfield
    Assinment: PA2
    Date: 3/3/2026
    
'''
import math

#theres gotta be a better way to do this
#maybe nest a dict, look into that

item_name = {"1": "Skittles",
             "2": "Resses",
             "3": "M&M",
             "4": "Chex",
             "5": "Honey",
             }

#since prices are hardcoded just shove them in a dict
prices = {"1": "100",
        "2": "119",
        "3": "150",
        "4": "99",
        "5": "199",
        }

display_prices = {"1": "$1.00",
                  "2": "$1.19",
                  "3": "$1.50",
                  "4": "$0.99",
                  "5": "$1.99",
}


    #stores coinage why the heck did i write this?
def coinage_store(coinage):
    coinage = float(coinage)
    a = coinage_convert(coinage)
    return a


#converts from float to int
def coinage_convert(money):
    intmoney = int(round(money, 5) * 100)
    return intmoney


#insert coins menu
def insert_coinage():
    global display_total
    global total
    quit = True
    print("Please enter:",
        "1.00 for $1 bill\n",
        "5.00 for $5 bills\n",
        ".01 for pennies\n",
        ".05 for nickels\n",
        ".10 for dimes\n",
        ".25 for quarters\n",
        "0 to cancel"
        )
    while quit == True:
        coinage = float(input("Enter in your money: "))
        coinage_quit = round(coinage, 1)
        if coinage_quit == 0:
            quit = False
            break

        else:
            coinage_1 = coinage + total
            print(coinage_1)
            total_update(coinage_1)
            print(coinage)
            print(total)
            print(f"Your current total is {display_total}.\nEnter 0 to stop deposit")
         
        
            
def purchase(item):
    global total
    #p_total = total
    item_price = (prices.get(item))
    disp_price = display_prices.get(item)
    print(f"**** This item costs {disp_price} ****")
    p_total = p_total - item_price
    total_update(p_total)
    


def purchase_menu():
    global quit_to_main
    total_update
    print(f"******** Total Money in machine is: {display_total} ********\n",
        "At any point if you wish to cancel operation or go back to last menu, please enter 0.\n",
        "Thank you!:",
        "If you would like to purchase:\n",
        "Skittles type '1', (Price = $1.00)\n",
        "Resse's type '2', (Price = $1.19)\n",
        "M&M's type '3', (Price = $1.50)\n",
        "Chex Mix type '4', (Price = $0.99)\n",
        "Honey Bun type '5'. (Price = $1.99)\n")
    item_entry = int(input("Your selection is: "))
    while item_entry != 0:
        purchase(item_entry)
        print(f"\n**** You have {display_total} left in the machine ****")
    else:
        quit_to_main = True
        
        


def main_menu():
    print("*********\n"
    "Welcome to this Vending Machine!\n",
    "*********\n\n",
    "If you would like to make a selection,\n",
    "please insert the appropriate currency into the machine.\n",
    )

def total_update(u_total):
    global total
    global display_total
    u_total = total + u_total

    #if u_total == 0:
    #    return "0"
    #calc the power of 10 needed
    #gets exponent of first digita
    #exponent = math.floor(math.log10(abs(u_total)))
    #factor to is 10 to the exponent
    #factor = 10 ** exponent
    #u_d_total = round((u_total // factor), 2)
   
    #returns with only two decimals trailing
    display_total = str("$" + (str({u_total})))



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
make a display total for amount left in machine
fix the decmials on display totals and item prices
complete purchase

write change function

'''


