import random
import gspread
from google.oauth2.service_account import Credentials
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))


def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))


def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))


def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))


def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))


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
        prYellow(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        prYellow("----------")
        prYellow(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        prYellow("----------")
        prYellow(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def getboard(self):
        """
        Get value of board
        """
        lista = "[ \n" + self.board[0] + "," + self.board[1] \
            + "," + self.board[2] + "," + "\n" + self.board[3] \
            + "," + self.board[4] + "," + self.board[5] \
            + "," + "\n" + self.board[6] + "," + self.board[7] \
            + "," + self.board[8] + "," + "\n ]"
        value = [self.username, self.currentPlayer, lista, self.winner]
        return value

    def playerinput(self):
        """"
        Gathers user input
        Checks if input is valid to open spot or not
        """""
        try:
            inp = int(input("Select a spot 1-9: "))
            if inp > 9 or inp < 1:
                # catch if user enters something not valid
                prRed("You need to enter a number between 1 and 9")
                self.playerinput()
            elif self.board[inp - 1] == "-":
                # space is available
                self.board[inp-1] = self.currentPlayer
            else:
                # user entered something that is already occupied
                prRed("Oops player is already at that spot.")
                self.playerinput()
        except ValueError:
            # catch if user enters a string
            prRed("You need to enter a number between 1 and 9")
            self.playerinput()

    def checkhorizontle(self):
        """
        Check for horizontal winner
        """
        if self.board[0] == self.board[1] == self.board[2] \
                and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        elif self.board[3] == self.board[4] == self.board[5] \
                and self.board[3] != "-":
            self.winner = self.board[3]
            return True
        elif self.board[6] == self.board[7] == self.board[8] \
                and self.board[6] != "-":
            self.winner = self.board[6]
            return True

    def checkrow(self):
        """
        Check for vertical winner
        """
        if self.board[0] == self.board[3] == self.board[6] \
                and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        elif self.board[1] == self.board[4] == self.board[7] \
                and self.board[1] != "-":
            self.winner = self.board[1]
            return True
        elif self.board[2] == self.board[5] == self.board[8] \
                and self.board[2] != "-":
            self.winner = self.board[2]
            return True

    def checkdiag(self):
        """
        Check for vertical winner
        """
        if self.board[0] == self.board[4] == self.board[8] \
                and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        elif self.board[2] == self.board[4] == self.board[6] \
                and self.board[4] != "-":
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
            exit()

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
            position = random.randint(0, 8)
            if self.board[position] == "-":
                self.board[position] = "0"
                self.switchplayer()

    def available_moves_display(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(str(i))
            else:
                moves.append(' ')
        return moves

    def available_moves(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')
