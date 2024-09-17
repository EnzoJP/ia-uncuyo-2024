def hill_climbing(board,max_states):
    punto_cinco=[]
    number_states = 0
    for indx in range(0,len(board.queens)): #recorro las reinas
        pairs = board.objective_function()
        ubication=board.queens[indx]
        i,j=ubication #posicion de la reina
        board.board[i][j] = 0
        best_move = (i, j)
        best_pairs = pairs
        for k in range(0,board.n):
            if k != i:  #sucesores en la columna
                board.board[k][j] = 1
                pairs_new = board.objective_function()
                punto_cinco.append(pairs_new)
                number_states += 1
                if pairs_new < pairs: #si el sucesor es mejor o igual
                    best_pairs = pairs_new
                    best_move = (k,j)
                board.board[k][j] = 0 
        board.board[best_move[0]][best_move[1]] = 1
        if best_pairs == 0:
            return board,number_states,False,punto_cinco
        else:
            if number_states > max_states:
                return board,number_states,True,punto_cinco #se alcanzo el maximo de estados retorno la mejor solucion encontrada hasta el momento
    return board,number_states,False,punto_cinco #no se encontro solucion     