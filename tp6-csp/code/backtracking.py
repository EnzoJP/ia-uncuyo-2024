def BackTracking(board, max_states):
    return BackTrackingRec(board, max_states, [])

def BackTrackingRec(board, max_states, states): #retorna solucion, truncado, tablero, cantidad de estados
    if len(states) >= max_states:
        return False, True, board, len(states)
    
    variable = select_unassigned_variable(board)
    
    if variable is None:
        return True, False, board, len(states)  # Solución encontrada
    
    domain_values = order_domain_values(board, variable)
    
    for value in domain_values:
        states.append(value)
        if is_consistent(board, variable, value):  # Verifica restricciones
            set_variable(board, variable, value)
            
                
            result, trunc, board, _ = BackTrackingRec(board, max_states, states)
                
            if trunc:
                return False, True, board, len(states)
                
            if result:
                return True, False, board, len(states) # Solución encontrada
            reset_variable(board, variable, value)
    
    return False, False, board, len(states)


def select_unassigned_variable(board):
    # Selecciona la primera columna sin reina
    for j in range(board.n):
        # Si en la columna no hay reina
        if 1 not in [board.board[i][j] for i in range(board.n)]:
            return j  # Retorna la columna no asignada
    
    return None  # Si todas las columnas ya tienen una reina, retornamos None


def order_domain_values(board, column): # Devuelve las posiciones posibles para la reina en la columna
    possible_values = []
    for i in range(board.n):
        if board.board[i][column] == 0:
            possible_values.append((i, column))
    return possible_values



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


def set_variable(board, column, value):
    for i in range(board.n):
        if board.board[i][column] == 1:  # Quita la reina de la fila actual
            board.board[i][column] = 0
    row, column = value
    board.board[row][column] = 1  # Coloca la reina en la nueva posición


def reset_variable(board, column, value): 
    row, column = value
    board.board[row][column] = 0  # Quita la reina de la posición



