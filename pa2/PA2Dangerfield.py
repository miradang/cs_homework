''' Name: Miranda Dangerfield
    Assinment: PA2
    Date: 3/3/2026
    
'''
import math

#theres gotta be a better way to do this
#maybe nest a dict, look into that

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



    #stores coinage why the heck did i write this?
#def coinage_store(coinage):
#    coinage = float(coinage)

    #former coinage convert function
#    a = int(round(coinage, 2) * 100)
#    return a


#converts from float to int
def coinage_convert(money):
    intmoney = int(round(money, 5) * 100)
    return intmoney


#insert coins menu
def insert_coinage():
    global display_total
    global int_total

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
        float_coinage = float(input("Enter in your money: "))
        #rounds coinage to 1 digit to see if its zero for quit condition
        #check to see if i need to return a quit value
        coinage_quit = round(float_coinage, 1)
        int_coinage = coinage_convert(float_coinage)

        if coinage_quit == 0:
            quit = False
            #quit condition

        else:
            total_add(int_coinage, float_coinage)
            print(f"Your current total is {float_total}.\nEnter 0 to stop deposit")
         
        
            
def purchase(item):
    global int_total
    global float_total
  
    item_price = products.get(item, {}).get("int_price")
    disp_price = products.get(item, {}).get("float_price")

    int_total = int_total - item_price
    float_total = float_total - disp_price
    print(f"**** This item costs {disp_price} ****")

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

    print(f"You have ${float_total} left in the machine ***",
    "Your change is:",
    "{quarters} Quarters",
    "{dimes} Dimes",
    "{nickles} Nickels",
    "{pennies} Pennies",
    )   


def purchase_menu():
    global quit_to_main
    print(f"******** int_total Money in machine is: {float_total} ********\n",
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
        if item_entry is range(1,6):
            purchase(item_entry)
            print(f"\n**** You have {float_total} left in the machine ****")
            item_entry = int(input("Your selection is: "))
        else:
            quit_to_main = True
        
    else:
        quit_to_main = True
        
        
def main_menu():
    print("*********\n"
    "Welcome to this Vending Machine!\n",
    "*********\n\n",
    "If you would like to make a selection,\n",
    "please insert the appropriate currency into the machine.\n",
    )

def total_add(int_coinage, float_coinage):
    global int_total
    global float_total

    int_total = int_coinage + int_total
    float_total = float_coinage + float_total

    print(f"totaladd {int_total}")
    #display_total = f"${int_total:.2f}"
    

def total_sub(int_coinage, float_coinage):
    global int_total
    global float_total

    int_total = int_total - int_coinage
    float_total = float_total - float_coinage

    print(f"totalsub {int_total}")
    #display_total = f"${int_total:.2f}"
    

#####global vars

#int_total in int
int_total = 0
#int_total as string
float_total = 0
display_total = ""
quit_to_main = False
#####End of global vars

######main programm loop#########
mainloop = True
while mainloop == True:
    main_menu()
    
    while quit_to_main == False:
        insert_coinage()
        
        print(int_total)
        purchase_menu()


'''
to do:
fix display int_total to show decimal points x
make a display int_total for amount left in machine x
fix the decmials on display totals and item prices x
complete purchase x

write change function x

write options def for loop

fix loop so you can bounce between main menu, insert, purchase, quit

'''


