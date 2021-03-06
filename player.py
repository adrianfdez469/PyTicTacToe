import random
from game import TicTacToe
import math


class Player:
    def __init__(self, letter):
        self.letter = letter
        self.wins = 0
        self.looses = 0
        self.ties = 0

    def get_move(self, game):
        pass

    def add_win(self):
        self.wins += 1

    def add_loose(self):
        self.looses += 1

    def add_tie(self):
        self.ties += 1


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game: TicTacToe):
        available_moves = game.available_moves()
        pos = random.choice(available_moves)
        print(f"Computer player choose {pos}")
        return pos


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game: TicTacToe):
        available_moves = game.available_moves()
        pos = None
        while pos not in available_moves:
            try:
                num = int(input("Enter a position [0, 8]"))
                if num not in available_moves:
                    raise ValueError
                pos = num
            except ValueError:
                print("Wrong input")
        return pos


class HardComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game: TicTacToe):
        available_moves = game.available_moves()
        if len(available_moves) == 9:
            square = random.choice(available_moves)
        else:
            square = self.minmax(game, self.letter)['position']
        print(f"Computer player choose {square}")
        return square

    def minmax(self, state, player):
        max_player = self.letter
        other_player = 'o' if player == 'x' else 'x'

        if state.winner == other_player:
            return {
                'position': None,
                'score': 1 * (state.num_empty_squares()+1) if other_player == max_player else -1 * (state.num_empty_squares()+1)
            }
        elif not state.empty_squares():
            return {
                'position': None, 'score': 0
            }

        if player == max_player:
            best = {
                'position': None, 'score': -math.inf
            }
        else:
            best = {
                'position': None, 'score': math.inf
            }

        for possible_move in state.available_moves():
            state.set_move(possible_move, player)
            sim_score = self.minmax(state, other_player)

            state.board[possible_move] = " "
            state.winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best

