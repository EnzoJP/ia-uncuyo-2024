from random import random,randint
from math import exp

#incluso con gpt no funciona como deberia 


def simulated_annealing(board, max_states):
    temperature = max_states
    initial_temperature = temperature
    number_states = 0
    
    for indx in range(0, len(board.queens)):  # Recorro las reinas
        pairs = board.objective_function()
        ubication = board.queens[indx]
        i, j = ubication  # Posición de la reina
        board.board[i][j] = 0
        best_move = (i, j)
        best_pairs = pairs
        
        for it in range(0, board.n):
            k = randint(0, board.n-1)
            while k == i:  # Evitar misma posición
                k = randint(0, board.n-1)
            
            board.board[k][j] = 1
            pairs_new = board.objective_function()
            delta = pairs_new - pairs
            
            temperature = schedule(temperature, initial_temperature)
            
            if delta > 0:  # Si el sucesor es mejor
                best_pairs = pairs_new
                best_move = (k, j)
            else:
                if random() < exp(delta / temperature):  
                    best_pairs = pairs_new
                    best_move = (k, j)
            
            number_states += 1
            board.board[k][j] = 0  
            
        board.board[best_move[0]][best_move[1]] = 1
        
        #  solución óptima
        if best_pairs == 0:
            return board, number_states, False
        
        
        if temperature < 1e-10: # doubdful
            return board, number_states, False
        
        
        if number_states > max_states:
            return board, number_states, True  # Retorno la mejor solución encontrada hasta el momento
    
    return board, number_states, False  # No se encontró solución

def schedule(t, initial_temperature, alpha=0.001):
    return initial_temperature / (1 + alpha * t)