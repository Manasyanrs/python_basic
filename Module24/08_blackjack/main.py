import random


class BlackJack:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"] * 4
        self.score = 0
        self.bot_score = 0

    def random_card(self):
        result = 0
        card = random.choice(self.deck)
        if card != "Ace":
            if isinstance(card, int):
                result += card
            else:
                result += 10
            self.deck.pop(self.deck.index(card))
        else:
            if self.score + 11 <= 21 or self.bot_score + 11 <= 21:
                result += 11
            else:
                result += 1
            self.deck.pop(self.deck.index(card))
        return result

    def play(self):
        while True:
            question = input("Взять карту y/n: ").lower()
            if question == "y":
                self.score += self.random_card()
                print("\nУ вас {} очков.".format(self.score))
                if self.score > 21:
                    break
                elif self.score == 21:
                    break
            else:
                bot = self.random_card()
                if self.bot_score + bot <= 16:
                    self.bot_score += bot
                elif self.bot_score == 21:
                    break
                else:
                    print("У вас {} очков.".format(self.score))
                    print("У крупье {} очков".format(self.bot_score))
                    break

    def winner(self):
        result = max(self.score, self.bot_score)
        if result == self.score:
            if result > 21:
                print("Вы проиграли")
            else:
                print("Вы выграли:")
        else:
            print("Выграл крупье")

    def print_info(self):
        for _ in range(2):
            score = self.random_card()
            bot_score = self.random_card()
            self.score += score
            self.bot_score += bot_score
        print("У вас {} очков.".format(self.score))

        self.play()
        self.winner()

    def start(self):
        self.print_info()


game = BlackJack()
game.start()
