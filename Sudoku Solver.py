import numpy as np
from random import randint



S= [
    [7,8,0,4,0,0,1,2,0], 
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,1,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

 # i is the number of rows while j is the number of columns



def solve(M): # this is the algorithm that will use all the other components to solve the matrix
    find= finder(M)
    if not find:
        return True
    else:
        row, col = find  
        # base of the algorithm. Will search for empty spaces, if it finds something it informs us
        # although once we reach the final square it means we have gone through every
        # every individual square and the solutions been found
    for i in range(1,10):
        if valid(M, i, (row, col)):
            M[row][col] = i
        # this will just try every possible solution between 1 and 9 in each square 
        # will check if it is a valid solution, and will add it to the board
            if solve(M):
                return True
    return False 
    # if we run through all the numbers and none work in  specific spot, we get False
    # which means we have to track back to the last square and try running the for loop
    # there again in order to find a different solution that will favour the next box








def valid(M, number, pos):

    # Check row first
    for i in range(len(M)): # goes through every column on the row
        if M[pos[0]][i] == number and pos[1] != i: 
            # checks if each position has gotten a number that we assigned
            # unless a number already exists there
            # then it skips over the filled boxes
            return False  
    
    #Check columns now aka vertically
    for j in range(len(M)):
        if M[i][pos[1]] == number and pos[0] != i:
            # does the same thing as in the rows but in the columns instead
            # hence we have the same code but swapped positions 
            return False
    # Check box

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y*3 + 3):
         for j in range(box_x * 3, box_x*3 + 3):
         # Break the matrix up into 9 boxes where row one is like 00, 01, 02
         # Row two is 10, 11, 12 and row three is 20, 21, 22
         # we multiply each position with 3, in both x and y directions, in order to 
         # arrive towards the later parts of the matrix where len is 6 or 7 or 8
         # we multiply by 3 in order to get there, so 02 times 3 will give us the the 6th element and so on
         # this way we can move through each element without having to divide the 9x9 up into 3x3s
            if M[i][j] == number and (i, j) != pos:
             #what this does is loop through the boxes and check ifany other element in the box
             # is equal to the one we just added and continue, also we make it known to not check 
             # the box where we just added the element
                return False 
            # if that's true we return flase because then we have found a duplicate

    return True 
    # if we make it thru all the checks then we have a valid element
    # we can move on


def print_board(M):


    for i in range(len(M)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - ")
# this adds a horizontal seperation between the boxes 
    for j in range(len(M[0])):
        if j % 3 == 0 and j != 0:
            print(" | ", end="")
# this adds a vertical seperation between the boxes
        if j == 8:
            print(M[i][j])
        # once it gets to the last element it understands that it has top stop and print now 
        # instead of continuing to draw lines both vertically or horizontally
        else:
            print(str(M[i][j]) + " ", end="")


def finder(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 0:
                return (i, j) 
            # This tool helps find the location of said empty space given by its row and column 
    return None


print_board(S)
solve(S)
print("______________________________")
print_board(S)