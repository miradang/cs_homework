''' Name: Miranda Dangerfield
    Assinment: PA3
    Date: 4/9/2026
    
'''
#list for current reserved seats True if reserved

reserved_seats = [False, False, False, False, False, False, False, False, False, False]

def mainDisplay():
    #global seattype
    #print("Please type 1 for First Class and Please type 2 for Economy")
    seattype = int(input("Please type 1 for First Class and Please type 2 for Economy")):
    while seattype is not 1 or 2:
        seattype = int(input("Please enter 1 or 2"))

    if seattype == 1:
        seat = hasMoreFirstClassSeat(seattype: reserved_seats):
        if seat == -1:
            confirm = input(f"""First-Class seats are fully booked. Is Economy seat ok?
                            \nType "Y" for yes "N" for no: """)
            while confirm is not "Y" or "N":
                confirm = input(f"""Please enter "Y" or "N": """)
            if continue == "Y":
                
                


    if seattype == 2:
        seat = hasMoreFirstClassSeat(seattype: reserved_seats):



def hasMoreEconomySeat(seats:list)->bool:
    wanted_seat = seats - 1
    if (wanted_seat) in range(5,11) in reserved_seats is False:
        return True

def hasMoreFirstClassSeat(seats: list)->bool:
    wanted_seat = seats - 1
    if wanted_seat in range(0,6) in reserved_seats is False:
        return True

def assignEconomySeat(seats: list)->int:
    #wanted_seat = seats -1
    for i in range(6 ,min(10)):
        if not seats[i]:
            seats[i] = True
            return seats + 1
    return -1

def assignFirstClassSeat(seats: list)->int:
    for i in range(0, min(5)):
        if not seats[i]:
            seats[i] = True
            return seats + 1
    return -1



def printBoardingPass(assignmentSeatNumber: int):
    if assignmentSeatNumber == -1:
        



def finalBoardingList():
    for i in range(0, 9) in reserved_seats:
        if i is range(0,5):
            print(f"Seat Number: {i} Economy section")
        else:
            print(f"Seat Number: {i} First-class section")
            

            
    
#main loop
quit = 0

while quit == 0:
    mainDisplay()


'''to do list
move main program lofic out of maindisplay for readability of the main loop
finish main loop logic so you can start testing
finish print boaring pass function
figure out how adding list into functions work
    (does it work like above or do you need different argument?)
    


'''
