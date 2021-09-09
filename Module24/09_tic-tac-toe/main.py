import random


class TicTacToe:
    winner_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    game_board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    numbers = [digit for digit in range(1, 10)]

    def __init__(self):
        self.suit = "X"
        self.bot = "0"

    def game_board_view(self):
        print("|{}|".format(11 * "-"))
        for row in self.game_board:
            print("|", end="")
            for column in row:
                print("", column, end=" |")
            print()
        print("|{}|".format(11 * "-"))

    def choice_of_suit(self):
        while True:
            suit = input("Выбирите масть Х или 0: ").upper()
            if suit == "X" and suit == "X":
                self.suit = "X"
                self.bot = "0"
                return suit
            elif suit == "0":
                self.suit = "0"
                self.bot = "X"
                return suit
            elif suit == "":
                return self.suit
            else:
                print("Выброть надо Х или 0")

    def play_bot(self, argument):
        bot_digit = 0
        if len(self.numbers) > 0:
            random_digit = random.choice(self.numbers)
            bot_digit += random_digit
            line = 0
            for element in self.game_board:
                if str(random_digit) in element:
                    self.game_board[line][element.index(str(random_digit))] = self.bot
                line += 1
            self.numbers.pop(self.numbers.index(random_digit))

        index = 0
        for combination in argument:
            if bot_digit in combination:
                argument[index][combination.index(bot_digit)] = self.bot
            index += 1

    def player(self, enter_number, argument):
        line = 0
        for element in self.game_board:
            if enter_number in element:
                self.game_board[line][element.index(enter_number)] = self.suit
            line += 1
        self.numbers.pop(self.numbers.index(int(enter_number)))

        index = 0
        for combination in argument:
            if int(enter_number) in combination:
                argument[index][combination.index(int(enter_number))] = self.suit
            index += 1

    def winner(self, argument):
        for element in argument:
            if element.count("X") == 3:
                return "X"
            if element.count("0") == 3:
                return "0"
            if len(self.numbers) == 0:
                return 0

    def play(self):
        print("Добро пожаловать в игру крестики нолики\n")
        self.choice_of_suit()
        flag = True
        while flag:
            self.game_board_view()
            try:
                number = input("Введите число (от 1 до 9) где хотитье поставить ваш масть: ")
                self.player(number, self.winner_combinations)

                self.play_bot(self.winner_combinations)

                if self.winner(self.winner_combinations) == self.suit:
                    print("\nВыиграл", self.suit)
                    self.game_board_view()
                    flag = False

                elif self.winner(self.winner_combinations) == self.bot:
                    print("\nВыиграл", self.bot)
                    self.game_board_view()
                    flag = False

                elif self.winner(self.winner_combinations) == 0:
                    print("\nИгра закочилься нечей")
                    self.game_board_view()
                    flag = False

            except ValueError:
                print("Данний номер занят")


game = TicTacToe()
game.play()
