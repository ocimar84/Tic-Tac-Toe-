# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from TicTacToeGame import TicTacToeGame
# import pyfiglet module
import pyfiglet
from colorama import Fore, Back, Style
print(Style.RESET_ALL)
print('back to normal now')

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))



result = pyfiglet.figlet_format("TIC TAC TOE", font = "bulbhead" )
print(result)



def play_game(game):
        """
        Start a tic-tac-toe game
        """
        while game.gameRunning:
            game.printboard()
            game.playerinput()
            game.checkifwin()
            game.checkiftie()
            game.switchplayer()
            game.computer()
            game.checkifwin()
            game.checkiftie()



def main():
        """"
        MAIN MENU FUNCTION
        """
        
        print(Back.GREEN + "Welcome to Tic-Tac-Toe!")
        while True:
            username = input("please enter a username: \n")
            if len(username.strip()) == 0:
                prRed("Invalid username")
                continue
            else:
                break
        prGreen(f"Hello {username}!")

        while True:
            to_play = input("Do you want to play a game? \n 1 = Yes\n 2 = No\n").strip().lower()
            if to_play == '2':
                prCyan(f"Thanks for play {username}, goodbye!")
                exit()
            elif to_play == '1':
                game = TicTacToeGame(username)
                play_game(game)
            else:
                print(Fore.RED +"You need to enter a valid entry.")
                continue


main()


if __name__ == '__main__':
    print("Hello")
