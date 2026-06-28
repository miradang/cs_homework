''' Name: Miranda Dangerfield
    Assinment: PA4
    Date: 5/1/2026
    
'''

def main():
    #user input total number of people
    while True:
        try:
            num_people = int(input("Enter the total number of people in the network: "))
            if num_people >= 1:
                break
            else:
                print("Please enter a number that is at least 1.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    #Store their names in a temp list
    names = []
    print("\n--- Enter Names ---")
    for i in range(num_people):
        #cleaning up trailing/leading spaces
        name = input(f"Enter the name for person {i + 1}: ").strip()
        names.append(name)

    #Creating an empty 2D list of size num_people x num_people
    list_of_friends = [[0 for _ in range(num_people)] for _ in range(num_people)]

    for i in range(num_people):
        for j in range(num_people):
            #you cant be freinds with yourself i = j
            if i == j:
                list_of_friends[i][j] = 0
            else:
                #calclate the lexicographic difference (thank god for wikipedia)
                #absolute difference of the first letter ASCII value
                #convert everything to lower case so we dont get weird results
                if len(names[i]) > 0 and len(names[j]) > 0:
                    char_i = names[i].lower()[0]
                    char_j = names[j].lower()[0]
                    diff = abs(ord(char_i) - ord(char_j))
                else:
                    diff = 0 #in case of empty string
                
                #Check if the difference is not greater than 12
                if diff <= 12:
                    list_of_friends[i][j] = 1
                else:
                    list_of_friends[i][j] = 0

    #Output the 2D list in a table
    print("\n--- Social Network Friendship Matrix ---")
    
    #print the top header row
    print("Names\t", end="")
    for name in names:
        print(f"{name}\t", end="")
    print() # Move to the next line

    #print the matrix rows
    for i in range(num_people):
        print(f"{names[i]}\t", end="")
        for j in range(num_people):
            print(f"{list_of_friends[i][j]}\t", end="")
        print() #Move to the next line after each row

    #Output the total number of friends each person has
    print("\n--- Total Friends Count ---")
    for i in range(num_people):
        #the sum of row i equals total friends for i
        total_friends = sum(list_of_friends[i])
        print(f"{names[i]} has {total_friends} friend(s).")

#main loop
if __name__ == "__main__":
    main()