''' Assignment: Fractions

   PA1Dangerfield.py

   Name: Miranda Dangerfield

   File Created on Feburary 27, 2026
'''

import math


#me being angry i have to put the function at the top of the program

def proper_fraction(num, den):
    if den == 0:
        print("The denominator cannot be zero.")
        return
    #checks if denominator is zero
    
    else:
        abs_num = abs(num)
        abs_den = abs(den)
        #gets absolute values of numerator and denominator for later
        
        if abs_num < abs_den:
            print(f"{abs(num)} / {abs(den)} is a proper fraction.")
            return
        #checks if its a basic fraction
        
        else:
            whole = abs_num // abs_den
            remain = abs_num % abs_den
            #gets the whole number for mixed fraction and remained for math later

            if remain == 0:
                print(f"{num} / {den} is an improper fraction and it can be reduced to {whole}")
                #output negative improper fractions show as -(a + b/c)
                return
            
        if remain != 0:
            divisor = math.gcd(remain, den)
            remain //= divisor
            simplified_den = den // divisor
        
        else:
            simplified_den = den
            #if remainder is zero puts it in output simp_den so i dont have to double up on it

        
        if num < 0:
            print(f"{num} / {den} is an improper fraction and its mixed fraction is -({abs(whole)} + {remain} / {simplified_den}).")
            return
            #output for negative improper fractions to convert it to postive as examples lists
        
        else:
            print(f"{num} / {den} is an improper fraction and its mixed fraction is {whole} + {remain} / {simplified_den}.")
            return
            #output for postive improper fractions

#quit condition
quit = 0

#main program loop
while quit == 0:

    print("\nThis program will tell you if a fraction is proper or improper.\n\tType q to quit.\n")
    
    num_a = input("Enter a numerator: ")
    if num_a == "q":
        break
    else:
        num_a = int(num_a)
    #checks input for q for quit condition if not true converts str to int

    den_a = input("Enter a denominator: ")
    if den_a == "q":
        break
    else:
        den_a = int(den_a)
    
    #calls the proper fraction function above
    proper_fraction(num_a, den_a)

           




    



             
