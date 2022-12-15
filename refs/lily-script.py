"""                                                                                                

Module connect_four contains the ConnectFour class, instances of which model Connect 4 games.      

(Seven columns, six rows.)

"""



class ConnectFour:


    def __init__(self, p1='pink', p2='purple'):

        """set up the player names and put them in self, then also make the oard and put it in self, as a list of lists [()]"""

        import pprint

        self.p1 = p1

        self.p2 = p2

        self.lol = [[None, None, None, None, None, None, None],

         [None, None, None, None, None, None, None],

         [None, None, None, None, None, None, None],

         [None, None, None, None, None, None, None],

         [None, None, None, None, None, None, None],

         [None, None, None, None, None, None, None]]

    def board(self):

        return tuple(tuple(row) for row in self.lol)

    def drop(self, col: int):

    # I was thinking abt setting up a counter here, so that the row cannot go over 1

    # (like cant have 2 plays in the same spot)

        for ply in range():

          self.lol.drop()

          if self.lol.drop([range(5, 0, -1)][col]) == None:

            self.lol.drop([range(5, 0, -1)][col]) == self.p1

            self.lol.drop([range(5, 0, -1)][col]) == self.p2

          else:

            raise ValueError