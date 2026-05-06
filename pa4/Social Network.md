Social Network  
Topics

String Methods, for-loop, 2-D list
Problem Description

You are intrigued by these social networking websites and want to know how they work. You started with figuring out your school’s social network. You want to know who is friend with who and how many friends each person has. Write a program that shows a two dimensional array of friends where each element taking a value of either 1 or 0 representing whether the person at row i is friends with person at column j. Your program should also output the number of friends each person has.
Programming Requirements

    Ask the user to enter the total number of people in the network to create the 2-D list (There should be at least 1 person in the network).
    Store their names in a separate list
    We will decide whether one person is friends with another if their names’ lexicographic difference is not greater than 12
    Populate the 2-D list with 1 representing row i and column j (jth element in each list represented by the row number) being friends and 0 representing row i and column j not being friends
    You should assume that you are not friends with yourself, which means that ListOfFriends[i][j] = 0, where i = j
    Output the 2-D list in a table format to the screen (use only tabs for spacing)
    Also output the total number of friends each person has (calculate using the 2-D list).

Note: A personal/assignment information block is required at the beginning of the source code. The following information should be included: your full name, assignment #, file name(s), due date.   

Example:

'''  Assignment: SocialNet

   Name: Paul Davis 

   File Created on March 10, 2024   

'''
Sample Outputs