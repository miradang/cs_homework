''' Assignment: Fractions

   PA1Dangerfield.py

   Name: Miranda Dangerfield

   File Created on Feburary 27, 2026
'''

import math

quit = 0

while quit == 0:

    print("This program will tell you if a fraction is proper or improper.\nType q to quit")
#figure out if you should convert to int or just store num/den as int for the quit condition
    num_a = int(input("Enter a numerator: "))
    if num_a == "q":
        break
    den_a = int(input("Enter a denominator:  "))
    if den_a == "q":
        break
    
    proper_fraction(num_a, den_a)

           
def proper_fraction(num, den):
    if den == 0:
        print("The denominator cannot be zero")
        return
    
    else:
        abs_num = abs(num)
        abs_den = abs(den)
        
        if abs_num < abs_den:
            print(f"{abs(num)} / {abs(den)} is a proper fraction")



    



             
