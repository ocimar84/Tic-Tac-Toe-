import random


class TicTacToeGame():

    def __init__(self, username):
        self.username = username
        self.currentPlayer = "X"
        self.winner = None
        self.gameRunning = True
        self.board = [
            "-", "-", "-",
            "-", "-", "-",
            "-", "-", "-",
        ]

    def printboard(self):
        """
        Prints the game board
        """
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("----------")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("----------")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def playerinput(self):
        """"
        Gathers user input
        Checks if input is valid to open spot or not
        """""
        inp = int(input("Select a spot 1-9: "))
        if self.board[inp - 1] == "-":
            self.board[inp-1] = self.currentPlayer
        else:
            print("Oops player is already at that spot.")
            self.playerinput()

    def checkhorizontle(self):
        """
        Check for horizontal winner
        """
        if self.board[0] == self.board[1] == self.board[2] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        elif self.board[3] == self.board[4] == self.board[5] and self.board[3] != "-":
            self.winner = self.board[3]
            return True
        elif self.board[6] == self.board[7] == self.board[8] and self.board[6] != "-":
            self.winner = self.board[6]
            return True

    def checkrow(self):
        """
        Check for vertical winner
        """
        if self.board[0] == self.board[3] == self.board[6] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        elif self.board[1] == self.board[4] == self.board[7] and self.board[1] != "-":
            self.winner = self.board[1]
            return True
        elif self.board[2] == self.board[5] == self.board[8] and self.board[2] != "-":
            self.winner = self.board[2]
            return True

    def checkdiag(self):
        """
        Check for vertical winner
        """
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        elif self.board[2] == self.board[4] == self.board[6] and self.board[4] != "-":
            self.winner = self.board[2]
            return True

    def checkifwin(self):
        """
        Check for winner
        """
        if self.checkhorizontle():
            self.printboard()
            print(f"The winner is {self.winner}!")
            self.gameRunning = False

        elif self.checkrow():
            self.printboard()
            print(f"The winner is {self.winner}!")
            self.gameRunning = False

        elif self.checkdiag():
            self.printboard()
            print(f"The winner is {self.winner}!")
            self.gameRunning = False

    def checkiftie(self):
        """
        Check if all spaces used
        """
        if "-" not in self.board:
            self.printboard()
            print("It is a tie!")
            self.gameRunning = False

    def switchplayer(self):
        """
        Switch between X and 0 player
        """
        if self.currentPlayer == "X":
            self.currentPlayer = "0"
        else:
            self.currentPlayer = "X"

    def computer(self):
        """
        Make a computer chose a random open space on board
        (computer is always 0)
        """
        while self.currentPlayer == "0":
            position = random.randint(0,8)
            if self.board[position] == "-":
                self.board[position] = "0"
                self.switchplayer()

