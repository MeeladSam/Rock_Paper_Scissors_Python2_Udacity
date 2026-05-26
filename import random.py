import random

moves = ['rock', 'paper', 'scissors']


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("Your move? (rock / paper / scissors): ").lower()
            if choice in moves:
                return choice
            print("  Oops! Please type rock, paper, or scissors.")

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def __init__(self):
        self.their_last = None

    def move(self):
        if self.their_last is None:
            return 'rock'
        return self.their_last

    def learn(self, my_move, their_move):
        self.their_last = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_last = None

    def move(self):
        if self.my_last is None:
            return 'rock'
        index = moves.index(self.my_last)
        return moves[(index + 1) % 3]

    def learn(self, my_move, their_move):
        self.my_last = my_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\n  You played: {move1}")
        print(f"  Computer played: {move2}")

        if move1 == move2:
            print("  It's a tie!")
        elif beats(move1, move2):
            print("  You win this round!")
            self.score1 += 1
        else:
            print("  Computer wins this round!")
            self.score2 += 1

        print(f"  Score -> You: {self.score1}  |  Computer: {self.score2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("\n  === Rock Paper Scissors ===\n")
        for round_num in range(1, 4):
            print(f"--- Round {round_num} ---")
            self.play_round()

        print("\n  === Final Score ===")
        print(f"  You: {self.score1}  |  Computer: {self.score2}")
        if self.score1 > self.score2:
            print("  You win the game! Congrats!")
        elif self.score2 > self.score1:
            print("  Computer wins the game. Better luck next time!")
        else:
            print("  It's a draw! Well played.")
        print()


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()