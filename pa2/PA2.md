Topics:
Input, Output, Operations, Decision, Repetition, 

Problem Description:
A vending machine is an automated machine that provides items such as snacks, beverages, and lottery tickets to consumers after cash, a credit card, or other forms of payment are inserted into the machine.

Currency deposit:

    The vending machine accepts 4 types of coins, 1 dollar bills, and 5 dollar bills, total 6 options.
    The user enters the money – simulate the action through a loop that ends when the user enters 0. Each coin, or paper bill will be read individually.
    The user can stop deposit at any time by entering 0.

Purchase item selection:

    The vending machine offers 5 products. The selections available for user are numbers from 1 to 5.  The user makes the selection, and the machine allows a maximum 4 other selections if the amount entered doesn’t cover the price of the item.  Refer item data listed below.

Skittles - type '1'     (Price = $1.00)
Reese’s - type '2'     (Price = $1.19)
M & M - type '3'     (Price = $1.50)
Chex Mix - type '4'    (Price = $0.99)
Honey Bun - type '5'     (Price = $1.99)

    The user can stop the item selection at any time by entering 0.
    Once an item is delivered, the machine gives the change in coins.
    Display the outcome of the operation for each alternative you consider possible for the vending machine.

Money change:

    The change is always given in coins, with maximum possible number of coins in each value: 25, 10, 5 or 1 cent.
    If the user chooses to cancel the selection by entering 0, the machine returns the initial amount in coins.
    Make sure that the machine returns the correct change in coins at all times.

Programming Requirements:

You are to write a program that simulates the functionality of a vending machine having the above characteristics. Use appropriate selection and repetition loops in your implementation.  


ttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt
Welcome to Vending Machine Bravo!
If you would like to make a selection,
please insert the appropriate currency into the machine.
Please enter:

If you would like to make a selection,
please insert the appropriate currency into the machine.
Please enter:
1.00 for $1 bills
5.00 for $5 bills
.01 for pennies
.05 for nickels
.10 for dimes
.25 for quarters
0 to cancel

    At any point if you wish to cancel operation or go back to last menu, please enter 0. Thank you!: 

5
***************** Total money in machine is: 5.00 *******************

    At any point if you wish to cancel operation or go back to last menu, please enter 0. Thank you!: 

If you would like to purchase:
Product A type '1', (Price = $1.00)
Product B type '2', (Price = $1.25)
Product C type '3', (Price = $1.50)
Product D type '4', (Price = $1.75)
Product E type '5'. (Price = $2.00)
Your enter is:
4
************ The item costs $1.75 *************
You have $3.25 left in the machine ***
Your change is:
13 Quarters
0 Dimes
0 Nickels

ttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt
Sample run:

Note: A personal/assignment information block is required at the beginning of the source code. The following information should be included: your full name, assignment #, file name(s), due date, purpose, honor code.    

Example:

''' Assignment: Fractions

   FractionsName.py

   Name: Paul Davis 

   File Created on March 10, 2024   

'''

Submission Requirements:

    Source code: Python file named as VendingYourlastname.py
    Project report: Include pseudocode, at least 5 screenshots of test runs in one PDF ﬁle and name it VendingYourlastname.pdf. 
