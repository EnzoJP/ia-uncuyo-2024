from copy import deepcopy

def FowardChecking (board,max_states):
    number_states = 0
    board_copi= deepcopy(board) #este tablero es solo para marcaje
    for col in range(board.n):
        if 0 not in [board_copi.board[i][col] for i in range(board.n)]: #no hay casillas vacias en la columna
            return False, False, board, number_states # no es solucion
        for row in range(board.n):
            number_states += 1
            if number_states >= max_states:
                return False, True, board, number_states
            if board.board[row][col] == 0 and is_consistent(board, col, (row, col)) and board_copi.board[row][col] != -1: #si la casilla esta vacia y es consistente
                #colocamos una reina
                board.board[row][col] = 1
                board_copi.board[row][col] = 1
                #actualizamos el tablero con las restricciones con un -1 en las casillas que no pueden tener reinas
                mark_inconsistent(board_copi, col, (row, col))
    return True, False, board, number_states

def is_consistent(board, variable, value):
    row, column = value
    
    # Verifica la fila y columna
    for i in range(board.n):
        if board.board[row][i] == 1 and i != column:  # Si hay una reina en la misma fila diferente a la columna actual
            return False
        if board.board[i][column] == 1 and i != row:  # mismo en fila
            return False
    
    # Verifica las diagonales
    for i in range(1, board.n):
        if row + i < board.n and column + i < board.n and board.board[row + i][column + i] == 1:
            return False
        if row - i >= 0 and column - i >= 0 and board.board[row - i][column - i] == 1:
            return False
        if row + i < board.n and column - i >= 0 and board.board[row + i][column - i] == 1:
            return False
        if row - i >= 0 and column + i < board.n and board.board[row - i][column + i] == 1:
            return False
    
    return True  # Si no hay conflictos, es consistente


def mark_inconsistent(board, variable, value):
    row, column = value
    #marcamos las casillas que no pueden tener reinas
    for i in range(board.n):
        if board.board[row][i] == 0 and i != column:
            board.board[row][i] = -1
        if board.board[i][column] == 0 and i != row:
            board.board[i][column] = -1
    for i in range(1, board.n):
        if row + i < board.n and column + i < board.n and board.board[row + i][column + i] == 0:
            board.board[row + i][column + i] = -1
        if row - i >= 0 and column - i >= 0 and board.board[row - i][column - i] == 0:
            board.board[row - i][column - i] = -1
        if row + i < board.n and column - i >= 0 and board.board[row + i][column - i] == 0:
            board.board[row + i][column - i] = -1
        if row - i >= 0 and column + i < board.n and board.board[row - i][column + i] == 0:
            board.board[row - i][column + i] = -1

    #board.print_board()
    return board