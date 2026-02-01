#fucking modulo
number = ()
quit = 'n'

while number != quit:
    number = (input("Enter n to stop. Enter a number and I will tell you if its is even or odd: "))
    
    if number != quit:
        number = int(number)
        if number % 2 == 0:
            print(f"{number} is even!")
        else:
            print(f"{number} is odd!")
    

