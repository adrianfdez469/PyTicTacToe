import time

from game import TicTacToe
from player import HumanPlayer, ComputerPlayer, UnbiteableComputerPlayer


def play(game: TicTacToe, player_o, player_x, print_game=True):
    letter = 'o'
    print(" __________")
    print("| NEW GAME |")
    print(" ----------")
    TicTacToe.print_board_numbers()
    while len(game.available_moves()) > 0 and game.winner is None:
        # pos = None
        if letter == 'o':
            print()
            pos = player_o.get_move(game)
            game.set_move(pos, letter)
            letter = 'x'

        else:
            #time.sleep(0.5)
            pos = player_x.get_move(game)
            game.set_move(pos, letter)
            letter = 'o'

        if print_game:
            game.print_board()

    if not print_game:
        game.print_board()
    if game.winner:
        print(f"Winer: {letter}")
        print()
        return letter
    else:
        print('It\'s a tie')
        print()
        return None


def runs(times):

    player_o = HumanPlayer('o')
    player_x = UnbiteableComputerPlayer('x')
    #player_o = ComputerPlayer('o')
    #player_x = ComputerPlayer('x')
    for _ in range(times):
        game = TicTacToe()
        winner = play(game, player_o, player_x)

        if winner == 'x':
            player_x.add_win()
            player_o.add_loose()
        elif winner is 'o':
            player_o.add_win()
            player_x.add_loose()
        else:
            player_x.add_tie()
            player_o.add_tie()

    print(f"Player: {player_x.letter} Wins: {player_x.wins} Losses: {player_x.looses} Ties: {player_x.ties}")
    print(f"Player: {player_o.letter} Wins: {player_o.wins} Losses: {player_o.looses} Ties: {player_o.ties}")


runs(1)

