# Author: Mahtab Zilaie
# Date: February 11, 2020
# Description: puzzle with a token on the leftmost square (of a list) token can shift left or right
# equal to the value in its current square but not allowed to move off the list. a recursive function
# determines if the puzzle is solvable by returning true of false for different lists.


def rec_row_puzzle(lst, token, visited):

    """helper function that takes the list, token, and visited spaces as parameters to determine if list is
    solvable"""

    if token < 0 or token >= len(lst):      # base case - if token is less than 0 or token is greater/equal to len lst
        return False
    if visited[token]:                  # base case- if same spot in visited is False
        return False
    if token == (len(lst) - 1):         # base case- if token reaches last index
        return True
    steps = lst[token]                   # sets steps to index in lst
    #print(steps)
    #print(lst)
    #print(visited)
    # visiting the token
    visited[token] = True  # changes visited to True from each spot visited by token
    return rec_row_puzzle(lst, token + steps, visited) or rec_row_puzzle(lst, token - steps, visited)
        # return either right or left steps and spots visited


def row_puzzle(lst):
    """function that takes only list as a parameter and sets values in helper function to decide if list is
     will return True or False"""

    visited = []             # sets visited to list
    for i in range(len(lst)):
        visited.append(False)    # for same range as list make a list with False spots
    return rec_row_puzzle(lst, 0, visited)  # sets list, token to 0, and visited

#lst = [2, 4, 5, 3, 1, 3, 1, 4, 0]
#print(row_puzzle(lst))
#lst2 =[1, 3, 2, 1, 3, 4, 0]
#print(row_puzzle(lst2))
