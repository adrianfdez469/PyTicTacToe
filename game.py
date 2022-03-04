class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.winner = None

    @staticmethod
    def print_board_numbers():
        for row in [[str((j*3)+i) for i in range(3)] for j in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [pos for pos, spot in enumerate(self.board) if spot is ' ']

    def check_winner(self, letter, pos):
        # Chequear si fila donde estoy esta con las 3 letras (x/o) del mismo tipo
        row_idx = pos // 3
        row = self.board[row_idx*3:(row_idx+1)*3]
        if all([sq == letter for sq in row]):
            return True

        #Chequear si columna donde estoy esta con las 3 letras (x/o) del mismo tipo
        col_ind = pos % 3
        col = [self.board[i*3+col_ind] for i in range(3)]
        if all([sq == letter for sq in col]):
            return True

        #Chequear diagonales
        diagonal1 = [ self.board[j] for j in [0, 4, 8]]
        if all([sq == letter for sq in diagonal1]):
            return True
        diagonal2 = [self.board[j] for j in [2, 4, 6]]
        if all([sq == letter for sq in diagonal2]):
            return True
        return False


    def set_move(self, pos, letter):
        self.board[pos] = letter
        # Check if {letter} wins
        if self.check_winner(letter, pos):
            self.winner = letter

    def num_empty_squares(self):
        return len(self.empty_squares())

    def empty_squares(self):
        return [sq for sq in self.board if sq == " "]