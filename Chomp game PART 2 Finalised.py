#A function that serves to introduce the players to the game. It presents the name of the game as well the instructions and rules for it.
def introduction():  # **ASK** Add to the main function
    print("Welcome to Chomp")
    print("Instructions:\nThis game challenges you to pick a number from the board. The number you choose will be "
          "\ndeleted as well as all numbers below it and to the right of it. The aim of the game is to avoid having to \n"
          "pick P, the poison. The players that ends up picking P looses the game. ©jajaultmate")

#A function which determines the size of playing board to be used in the game. The user chooses how big the board is
def board_size():
    #A variable which is used in a while-loop to make sure that the user inputs positive numbers when creating the board
    number_not_positive = 0
    while number_not_positive < 1:
        number_of_rows = int(input("How many rows do you want?"))
        number_of_columns = int(input("How many columns do you want?"))
        if number_of_rows < 0 or number_of_columns < 0:
            print("Negative numbers are not accepted, please try again")
            continue
        else:
            number_not_positive += 1
    return number_of_rows, number_of_columns


#A function which creates the actual board from the information gathered from the previous function, board_size()
def create_chocolate_bar(rows, columns):
    #An empty list to be filled with sublists
    board_list = []
    #A for-loop that goes through every value between the range of 1 and the number of rows the user chooses at the start
    for i in range(1, rows + 1):
        #An empty list is created that will be the sublist to be put inside the bigger list, board_list
        sublist = []
        #For-loop which goes through every value to be fed in to the sublist with the appropriate calculation
        for j in range(1, columns + 1):
            every_column = j + i * 10
            sublist.append(str(every_column))
        board_list.append(sublist)
        #Replaces what would be the number 11 to P, which stands for Poison
    board_list[0][0] = "P "
    return board_list


#A function that prints out the board to be displayed for the user
def print_chocolate_bar(list_of_current_board):
    #A for-loop that goes through the number of sublists inside the bigger list.
    for i in range(len(list_of_current_board)):  # Alternatively use print(*i) where "i" is an variable
        #A for-loop which goes through every value inside the current sublist and assigns it the variable j
        for j in list_of_current_board[i]:
            #A print-statement with format to create a user friendly and appealing board to use
            print('{:3s}'.format(j),end=" ")#print(j, end=" ")
        print("")


#A function which takes care of the main component of the game, to delete the appropriate numbers from the playing board
def chomp(list_of_current_board, sublist_to_chomp, starting_value_to_chomp):
    #A for-loop that goes the range from the sublist in which the number the usr picked is in through the rest of the sublists
    for i in range(sublist_to_chomp, len(list_of_current_board)):
        #A list to keep track of the numbers that have been "chomped" so to keep track and inform the user that those numbers are not available
        list_of_used_numbers = [list_of_current_board[i][starting_value_to_chomp:]]
        #Deletes the appropriate values from the big list according to the game's logic
        del list_of_current_board[i][starting_value_to_chomp:]
    return list_of_current_board, list_of_used_numbers

#A function that checks if the game has finished, which it does if the board only has P left
def check_winner(list_of_current_board):
    #If-statements to check if the requirements for the game to end are met
    if list_of_current_board == [["P "]]:
        return True
    elif len(list_of_current_board) <= 1 and len(list_of_current_board[0]) >= 1:
        return False
    elif list_of_current_board[0] == ["P "] and not any(list_of_current_board[1:]):
        return True
    return False

#A function which takes care of asking the user to pick a number to "chomp"
def ask_cell_number(list_of_current_board, list_of_used_numbers, player_turn):
    #A variable to help with the while-loop to determine when to run
    valid = False
    while valid == False:
        if player_turn % 2 == 0:
            print("Player 2's turn")
        else:
            print("Player 1's turn")
        user_choice = input("Choose a number from the board:")
        #A try-statement that tries to go through the big list in the same manner as the function print_chocolate_bar() so to be able to get the position of that number to pass on to the function chomp()
        try:
            for y in range(len(list_of_used_numbers)):
                for x in range(len(list_of_used_numbers[y])):
                    if user_choice == x:
                        print("That number has already been used, please try again")
                        continue
            for i in range(len(list_of_current_board)):
                for j in range(len(list_of_current_board[i])):
                    check_number_valid = list_of_current_board[i][j]
                    if check_number_valid == user_choice:
                        valid = True
                        return i, j
            raise ValueError
        except ValueError:
            print("The number you chose is not available, please try again.")
            continue

#A function which runs all other functions together
def main():
    introduction()
    number_rows, number_columns = board_size()
    board_game = create_chocolate_bar(number_rows, number_columns)
    print_chocolate_bar(board_game)
    validity = check_winner(board_game)
    used_numbers = []
    player_turn = 1
    #A while-loop which keeps the game running as long as there are still numbers to pick from the board
    while validity == False:
        row, col = ask_cell_number(board_game, used_numbers, player_turn)
        board_game, used_numbers = chomp(board_game, row, col)
        check_winner(board_game)
        print_chocolate_bar(board_game)
        player_turn += 1
        #An if-statement which checks if the check_winner() function returns True. When it does it presents the winner of the game and breaks the loop thus ending the program
        if check_winner(board_game) == True:
            if player_turn % 2:
                print("Player 2 won the game")
            else:
                print("Player 1 won the game")
            break
        else:
            continue
main()