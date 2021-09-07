import random


class TicTacToe:
    game_board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    numbers = [digit for digit in range(1, 10)]

    def __init__(self):
        self.suit = "X"
        self.bot = "0"

    def choice_of_suit(self):
        while True:
            suit = input("Выбирите масть Х или 0: ").upper()
            if suit == "X" and suit == "X" or suit == "0":
                self.bot = "0"
                return suit
            elif suit == "":
                return self.suit
            else:
                print("Выброть надо Х или 0")

    def game_board_view(self):
        print("|{}|".format(11 * "-"))
        for row in self.game_board:
            print("|", end="")
            for column in row:
                print("", column, end=" |")
            print()
        print("|{}|".format(11 * "-"))

    def winner(self, argument):
        # TODO не используем \ для переноса, попробуйте применить цикл
        if self.game_board[0][0] == self.game_board[1][0] == self.game_board[2][0] == argument or \
                self.game_board[0][1] == self.game_board[1][1] == self.game_board[2][1] == argument or \
                self.game_board[0][2] == self.game_board[1][2] == self.game_board[2][2] == argument or \
                self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] == argument or \
                self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] == argument or \
                self.game_board[0][0] == self.game_board[0][1] == self.game_board[0][2] == argument or \
                self.game_board[1][0] == self.game_board[1][1] == self.game_board[1][2] == argument or \
                self.game_board[2][0] == self.game_board[2][1] == self.game_board[2][2] == argument:
            return self.suit

        elif self.game_board[0][0] == self.game_board[1][0] == self.game_board[2][0] == self.bot or \
                self.game_board[0][1] == self.game_board[1][1] == self.game_board[2][1] == self.bot or \
                self.game_board[0][2] == self.game_board[1][2] == self.game_board[2][2] == self.bot or \
                self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] == self.bot or \
                self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] == self.bot or \
                self.game_board[0][0] == self.game_board[0][1] == self.game_board[0][2] == self.bot or \
                self.game_board[1][0] == self.game_board[1][1] == self.game_board[1][2] == self.bot or \
                self.game_board[2][0] == self.game_board[2][1] == self.game_board[2][2] == self.bot:
            return self.bot
        else:
            if len(self.numbers) == 0:
                return 0

    def play(self):
        print("Добро пожаловать в игру крестики нолики\n")
        suit = self.choice_of_suit()
        while True:
            self.game_board_view()
            try:
                number = input("Введите число (от 1 до 9) где хотитье поставить ваш масть: ")
                self.numbers.pop(self.numbers.index(int(number)))
                bot_digit = ""
                if len(self.numbers) > 0:
                    bot_number = str(random.choice(self.numbers))
                    bot_digit += bot_number

                line = 0
                for element in self.game_board:
                    if number in element:
                        self.game_board[line][element.index(number)] = suit

                    if bot_digit in element:
                        self.game_board[line][element.index(bot_digit)] = self.bot
                        self.numbers.pop(self.numbers.index(int(bot_digit)))
                    line += 1

            except ValueError:
                print("Данний номер занят")
            finally:
                if self.winner(suit) == self.suit:
                    print("\nВыиграл", self.suit)
                    self.game_board_view()
                    break
                elif self.winner(suit) == self.bot:
                    print("\nВыиграл", self.bot)
                    self.game_board_view()
                    break
                elif self.winner(suit) == 0:
                    print("Игра закончился ничьей")
                    self.game_board_view()
                    break


game = TicTacToe()
game.play()

# TODO если выбрать нолики то Х не ставиться
