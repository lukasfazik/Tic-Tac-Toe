import os
from random import randint


class Board:

    def __init__(self):
        """
        Creates empty board
        Board is list with first index empty and then indexes from 1 to 9 are used as positions on the board.
        """
        self.board = [None] + list(" " * 9)

    def tutorial_board(self):
        """
        Displays tutorial board. Tutorial board has numbers instead of values from Board.board
        """
        board = [None] + list(range(1, 10))
        print(f" {board[7]} | {board[8]} | {board[9]} ")
        print("-----------")
        print(f" {board[4]} | {board[5]} | {board[6]} ")
        print("-----------")
        print(f" {board[1]} | {board[2]} | {board[3]} ")

    def display(self):
        """
        Prints the board on the screen, uses board data from list at self.board
        """
        board = self.board
        print("\nBoard:")
        print(f" {board[7]} | {board[8]} | {board[9]} ")
        print("-----------")
        print(f" {board[4]} | {board[5]} | {board[6]} ")
        print("-----------")
        print(f" {board[1]} | {board[2]} | {board[3]} ")

    def set(self, player, position):
        """
        Sets the symbol to the board column.
        :param player: player object with symbol attribute
        :param position: symbol will be added to this position in the board
        :return: Returns string 'position occupied' if there is already symbol in desired board position
        """
        if self.board[position] == " ":
            self.board[position] = player.symbol
            return
        else:
            print(f"Board position {position} is already occupied. Choose another position.")
            return 'position occupied'

    def init(self):
        """
        Initialize board to default empty configuration
        """
        self.__init__()


class Player:
    def __init__(self, name, symbol):
        """
        Assigns name and symbol to player object, called from ask_for_player_names_and_symbol()
        :param name: String
        :param symbol: String "X" or "O"
        """
        self.name = name
        self.symbol = symbol

    def win(self):
        """
        Prints who has won the game
        """
        print(f"{self.name} has won the game.")
        game.stop()

    def turn(self):
        """
        Ask player on turn to input desired symbol location on the board.
        """
        while True:
            try:
                position = int(input(f"\n{self.name} choose the symbol position on the board (1 - 9): "))
            except ValueError:
                print("You haven't entered a number! Try again.")
                continue
            if position not in range(1, 10):
                print("You have entered a number not in range between one and nine.")
                continue
            else:
                if board.set(self, position) == "position occupied":
                    continue
                break


class Game:

    def __init__(self):
        self.running = False
        self.player_on_turn = None

    def random_first_player(self):
        self.player_on_turn = randint(1, 2)
        print("Random number generator decided that:")
        if self.player_on_turn == 1:
            print(f"{player1.name.capitalize()} begins the game.")
        else:
            print(f"{player2.name.capitalize()} begins the game.")

    def turn_logic(self):
        """
        Uses player attribute player_on_turn to decide which player is going to turn.
        """
        if self.player_on_turn == 1:
            self.player_on_turn = 2
            player1.turn()
        else:
            self.player_on_turn = 1
            player2.turn()

    def start(self):
        """
        Start function that prepares the game
            - Initialise object board from class Board
            - Prints information about how to to play the game + tutorial board
            - sets Game.running to True
            - chooses randomly the first player of the game using Game.random_first_player()
        """
        global board
        board = Board()
        print("During the game you will choose your symbol location on the board using number from 1 to 9."
              "\n\nBelow are displayed numbers according to board positions:\n")
        board.tutorial_board()
        input("\nPress ENTER to continue.")
        clear_screen()
        game.running = True
        self.random_first_player()
        board.display()

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            self.turn_logic()
            clear_screen()
            board.display()
            if self.check_win(board.board, player1):
                player1.win()
            elif self.check_win(board.board, player2):
                player2.win()
            else:
                self.check_draw()

    def check_draw(self):
        if " " not in board.board:
            print("Draw! Congrats to both players :)")
            game.stop()

    def check_win(self, board, player):
        symbol = player.symbol
        return ((board[7] == board[8] == board[9] == symbol) or  # across the top
                (board[4] == board[5] == board[6] == symbol) or  # across the middle
                (board[1] == board[2] == board[3] == symbol) or  # across the bottom
                (board[7] == board[4] == board[1] == symbol) or  # down the middle
                (board[8] == board[5] == board[2] == symbol) or  # down the middle
                (board[9] == board[6] == board[3] == symbol) or  # down the right side
                (board[7] == board[5] == board[3] == symbol) or  # diagonal
                (board[9] == board[5] == board[1] == symbol))  # diagonal


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ask_for_player_names_and_symbol():
    """
    From user input sets up players objects player1, player2 with name attributes and symbols attributes
    """
    global player1, player2
    player1_name = input("Input the name of the first player (Player 1): ")
    if player1_name == '':
        player1_name = "Player 1"
    while True:
        player1_symbol = (input(f"Choose the symbol of a player {player1_name} (X/o): ")).upper()
        if player1_symbol == "X" or player1_symbol == "O" or player1_symbol == "":
            if player1_symbol == "O":
                player2_symbol = "X"
            else:
                player1_symbol = "X"
                player2_symbol = "O"
            break
        else:
            print("You have entered a wrong symbol!\n")
            continue
    player2_name = input("Input the name of the second player (Player 2): ")
    if player2_name == "":
        player2_name = "Player 2"
    player1 = Player(player1_name, player1_symbol)
    player2 = Player(player2_name, player2_symbol)
    print(f"\n{player1.name} = {player1.symbol}")
    print(f"{player2.name} = {player2.symbol}")


if __name__ == '__main__':
    """
    Initialise the game object. And run the game.
    """
    again = True
    game = Game()
    print("Welcome in tic-tac-toe game by YOSHI :)\n")
    ask_for_player_names_and_symbol()
    while again:
        game.start()
        game.run()
        while True:
            decision = input("Do you want to play again? (YES/no): ").upper()
            if decision in ["", "Y", "YES"]:
                clear_screen()
                break
            elif decision in ["N", "NO"]:
                print("Thanks for the game. Bye :)")
                again = False
                break
            else:
                clear_screen()
                print("Wrong answer!")
                again = True
                continue
