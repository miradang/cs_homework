# Assignment: Fractions
# PA1Dangerfieldpy.py
# Name: Miranda Dangerfield
# File Created on October 12, 2025 
# Due Date: 10/12/2025
# Purpose: writing a program that calculate and displays proper/improper fractions 

#easist way to find GCD is with math module
import math

#Input
num1 = int(input("Enter a Numerator: "))
den1 = int(input("Enter a Denominator: "))

#Validate den1 input
if den1 == 0:
        print("denominator cannot be zero.")
else:
    #get absolute value for numbers for later
    abs_num = abs(num1)
    abs_den = abs(den1)

#see if fraction is proper or improper
if abs_num < abs_den:
            #proper fraction
            print(f"{abs(num1)} / {abs(den1)} is a proper fraction")
else:
    whole = num1 // den1
    remain = abs(num1 % den1)
    
#implify fraction part if remainder exists
    if remain != 0:
        divisor = math.gcd(remain, den1)
        remain //= divisor
        simplified_den = den1 // divisor
        
    else: simplified_den = den1

#output for mixed or whole number
    if remain == 0:
        print(f"{num1} / {den1} is an improper fraction and it can be reduced to {whole}")
        #output negative improper fractions show as -(a + b/c)
    elif num1 < 0:
        print(f"{num1} / {den1} is an improper fraction and its mixed fraction is -({abs(whole)} + {remain} / {simplified_den}).")
    else:
        print(f"{num1} / {den1} is an improper fraction and its mixed fraction is {whole} + {remain} / {simplified_den}.")

