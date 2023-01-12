# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from TicTacToeGame import TicTacToeGame



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
        print("Welcome to Tic-Tac-Toe!")
        while True:
            username = input("please enter a username: \n")
            if len(username.strip()) == 0:
                print("Invalid username")
                continue
            else:
                break
        print(f"Hello {username}!")

        while True:
            to_play = input("Do you wuant to play a game? \n 1 = Yes\n 2 = No\n").strip().lower()
            if to_play == '2':
                print(f"Thanks for play {username}, goodbye!")
            elif to_play == '1':
                game = TicTacToeGame(username)
                play_game(game)
            else:
                print("You need to enter a valid entry.")
                continue


main()


if __name__ == '__main__':
    print("Hello")
