# explain game
print('==============================================================================')
print('==============================================================================')
print(' ')
print('welcome to a very rudimentary connect 4 game in python')
print('the goal of the game is to get 4 tiles in a row')
print("player 1 is 'X' and player 2 is 'O'")
print("players can enter values of 1-7 to signify which column they would like to drop their tile, press 'ender' to drop")
print(' ')
print('the author also invites you to check out his website, calday.one, feel free to send feedback to cal@calday.one!')
print('enjoy!')
print(' ')
print('==============================================================================')
print('==============================================================================')

# define the template for the 'game' object (customized data class)
class C4Model:

    # the initial constructor for the c4 game object
    def __init__(self, p1, p2,):
        self.p1 = p1
        self.p2 = p2
        self.gameBoard = [
            ['','','','','','',''],
            ['','','','','','',''],
            ['','','','','','',''],
            ['','','','','','',''],
            ['','','','','','',''],
            ['','','','','','',''],
            ['','','','','','','']
        ]
        self.isComplete = False
        self.currentPlayer = 'player 1'
        self.lastMove = ''

    # function that takes the board array of arrays and prints the board as a string that is readable in the console
    def printBoard(self):
        print('\n 0 1 2 3 4 5 6\n', end="")
        for row in self.gameBoard:
            print('|', end="")
            for slot in row:
                if (slot == ''):
                    print('', end='_|')
                else:
                    print(slot, end='|')
            print('')
            
    # function that returns weather or not the game is still in play
    def __bool__(self):
        return False

    # function that allows one of the players to drop their tile by specifying a number 1-7 for the column
    def drop(self, move):
        print('cool')
    
    # function that returns the board as an array of 6 items representing the rows, with each item being its own array of 7 items representing individual slots
    def board(self):
        print('this is board')
        return self.gameBoard

    # function that returns a hash table (dict) with two items mapping the player numbers (1 & 2) to their respective names / colors
    def player_names():
        player_dict = {
            1: {
                'name': 'player 1',
                'color': 'blue'
            },
            2: {
                'name': 'player 2',
                'color': 'orange'
            }
        }
        return player_dict

    # function that returns the winner of the game, or 'none' if the game has not ended or has ended in a draw
    def winner():
        return None



#============================================================
#============================================================

# initialize a new game 'g' based on the connect 4 model above
g = C4Model(p1='red', p2='orange')


while (g.isComplete == False):
    g.printBoard()
    print("\n" + g.currentPlayer + " make your move")
    move = input()

    # run the drop method
    g.drop(move)


    if (g.currentPlayer == 'player 1'):
        g.currentPlayer = 'player 2'
    else:
        g.currentPlayer = 'player 1'


