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

    def __init__(game):
        game.p1 = 'player 1'
        game.p2 = 'player 2'
        game.rows = [
            ['','','','','','',''],
            ['','','','','','',''],
            ['','','','','','',''],
            ['','','','','','',''],
            ['','','','','','',''],
            ['','','','','','',''],
            ['','','','','','','']
        ]

    # function that takes the boad array of arrays and prints the board as a string that is readable in the console
    def __str__():
        print('here are the rows lol')

    # function that returns weather or not the game is still in play
    def __bool__():
        return False

    # function that allows one of the players to drop their tile by specifying a number 1-7 for the column
    def drop(player):
        print('cool')
    
    # function that returns the board as an array of 6 items representing the rows, with each item being its own array of 7 items representing individual slots
    def board():
        print('cool')

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