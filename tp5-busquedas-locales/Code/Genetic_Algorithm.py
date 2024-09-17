from random import randint,sample
from board import Board

    #Individuos: son los 30 tableros iniciales de cada tamaño
    #Seleccion: se seleccionan los 15 mejores individuos
    #Crossover: se cruzan los 15 mejores individuos(cada par de individuos se cruza en un punto)
    #remplazo: la nueva generacion suma los 20 mejores hijos y los 5 mejores padres(mutados)
    #fitness: cantidad de pares de reinas atacandose (funcion en board)
    #mutacion: se mutan remplazando una reina por otra al azar en la misma columna con probabilidad 0.8
    #condicion de parada: cantidad de iteraciones


def genetic_algorithm(list_boards, max_iter):
    
    for it in range(max_iter):
        list_boards.sort(key=lambda x: x.objective_function())  # Ordenar por fitness
        if list_boards[0].objective_function() == 0:  # Solución óptima 
            return list_boards[0], it
        
        selected_boards = list_boards[:15]  # Selección de los 15 mejores
        
        # Crossover
        new_boards = []
        for i in range(0, len(selected_boards)-1):
            point1 = randint(1, selected_boards[i].n-1)
            point2 = randint(1, selected_boards[i].n-1)
            new_board1, new_board2 = crossover(selected_boards[i], selected_boards[i+1], point1, point2)
            new_boards.append(new_board1)
            new_boards.append(new_board2)
        
        # Mutación
        list_boards.sort(key=lambda x: x.objective_function())
        list_boards.reverse()
        for i in range(0, len(list_boards)-1):  # Mutar los 10 peores
            if randint(0, 10) < 8:
                list_boards[i] = mutar(list_boards[i])
        
        new_boards.sort(key=lambda x: x.objective_function())
        

        # Reemplazo
        list_boards = new_boards[:20] + list_boards[:5] # 20 mejores nuevos + 5 mejores antiguos (mutados)
        
    return list_boards[0], max_iter  # Mejor individuo al final de las iteraciones

def mutar(individuo):
    n = individuo.n
    j = randint(0, n-1)  
    i = randint(0, n-1)  
    # Mover la reina de la columna j a una nueva fila i
    for k in range(n):
        if individuo.board[k][j] == 1:
            individuo.board[k][j] = 0
            individuo.board[i][j] = 1
            break
    return individuo

def crossover(individuo1, individuo2, point1, point2):
    n = individuo1.n
    new_individuo1 = Board(n)
    new_individuo2 = Board(n)
    
    for j in range(n):
        if point1 <= j < point2:
            for i in range(n):
                new_individuo1.board[i][j] = individuo1.board[i][j]
                new_individuo2.board[i][j] = individuo2.board[i][j]
        else:
            for i in range(n):
                new_individuo1.board[i][j] = individuo2.board[i][j]
                new_individuo2.board[i][j] = individuo1.board[i][j]
    
    return new_individuo1, new_individuo2


def torneo_seleccion(list_boards, k=15):
    torneo = sample(list_boards, k)
    torneo.sort(key=lambda x: x.objective_function())
    return torneo[:15]
