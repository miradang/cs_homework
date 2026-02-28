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
    
    else:
        abs_num = abs(num)
        abs_den = abs(den)
        
        if abs_num < abs_den:
            print(f"{abs(num)} / {abs(den)} is a proper fraction.")
            return
        
        else:
            whole = num // den
            remain = abs(num % den)

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

        if num < 0:
            print(f"{num} / {den} is an improper fraction and its mixed fraction is -({abs(whole)} + {remain} / {simplified_den}).")
            return
        else:
            print(f"{num} / {den} is an improper fraction and its mixed fraction is {whole} + {remain} / {simplified_den}.")
            return

#quit condition
quit = 0

#main program loop
while quit == 0:

    print("\nThis program will tell you if a fraction is proper or improper.\n\tType q to quit.\n")
#figure out if you should convert to int or just store num/den as int for the quit condition
    num_a = int(input("Enter a numerator: "))
    if num_a == "q":
        break
    den_a = int(input("Enter a denominator: "))
    if den_a == "q":
        break
    
    #calls the proper fraction function above
    proper_fraction(num_a, den_a)

           




    



             
