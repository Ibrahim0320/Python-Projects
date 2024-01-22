# making a simple tic tac toe game for two players

board= [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]



class player:
    def __init__(self, symbol):
        self.symbol= symbol








def display(board):
    for row in board:
        print(' | '.join(map(str,row)))
    if row != board[-1]:
        print('-----------------')





def player_input(current_player):
    position = input(f'Player {current_player.symbol}, choose a position (1-9)')
    return int(position)





def update(board, position, player):


    for row in board:
        for i in range(len(row)):
            if row[i] == position:
                row[i] = player.symbol
    



def space_check(board, position):
    for row in board:
        for i in range(len(row)):
            if row[i] == position:
                return True
    return False




def win_check(board, current_player):

    for row in board:
        if row[0] == row[1] == row[2] == current_player.symbol:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == current_player.symbol:
            return True
    if board[0][0] == board[1][1] == board[2][2] == current_player.symbol or board[0][2] == board[1][1] == board[2][0] == current_player.symbol:
        return True
    
    return False

def win(current_player):
    if win_check(board, current_player):
        display(board)
        print(f'Player {current_player.symbol} wins!')



def tie_check(board):
    for row in board:
        for cell in row:
            if cell not in ('X', 'O'):
                return False
    return True

def tie():
    display(board)
    print('The game is a tie!')


def game():
    print("Welcome to TicTacToe")
    player1= player('X')
    player2= player('O')
    current_player= player1

    while True:
        
        display(board)
        position= player_input(current_player)


        while not space_check(board, position):
            print('Invalid position. Choose again.')
            position= player_input(current_player)


        update(board, position, current_player)

        if win_check(board, current_player):
            win(current_player)
            break
        if tie_check(board):
            tie()
            break
        current_player = player2 if current_player== player1 else player1



game()




 