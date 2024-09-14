#Problema de las 9 reinas con buqueda local

from board import Board
from random import randint,seed
from Hill_Climbing import *
from Simulated_Annealing import *
from Genetic_Algorithm import *
from copy import deepcopy
from time import time
import csv
from utils import *

def main():

    #creo los tableros y los guardo en una lista 30 por cada tamaño
    sizes = [4,8,10]
    boards = []
    iterations = 30
    for size in sizes:
        for i in range(iterations):
            #creo un tablero
            board = Board(size)
            board.random_board()
            boards.append(board)

    #probamos los algoritmos en los tableros creados
    print("--------Hill Climbing------")

   
    for board in boards:
        board_cop = deepcopy(board) #copio para no modificar el original
        print("Numero de tablero: ", boards.index(board)+1)
        print("longitud del tablero: ", board.n)
        #board.print_board()
        first_queens = board.objective_function()
        print("Cantidad de reinas atacandose (pares): ", first_queens)
        print("Solucion")
        
        start=time()
        max_states = 100
        board_sol,number_states,truncated = hill_climbing(board_cop,max_states)
        end=time()
        if truncated:
            #board_sol.print_board()
            queens_sol=board_sol.objective_function()            
            print("El algoritmo fue truncado por alcanzar el maximo de estados")
            print("Cantidad de pares de reinas atacandose: ", queens_sol)
            print("cantidad de estados explorados: ", number_states )           
            guardar_resultados_csv(file,board_sol.n,"Hill Climbing",truncated,number_states,end-start)
        else:
            #board_sol.print_board()
            queens_sol=board_sol.objective_function()
            print("Cantidad de pares de reinas atacandose: ", queens_sol)
            print("cantidad de estados explorados: ", number_states)
            guardar_resultados_csv(file,board_sol.n,"Hill Climbing",truncated,number_states,end-start)
        
    print("--------Simulated Annealing------")


    for board in boards:
        board_cop = deepcopy(board) #copio para no modificar el original
        print("Numero de tablero: ", boards.index(board)+1)
        print("longitud del tablero: ", board.n)
        board.print_board()
        first_queens = board.objective_function()
        print("Cantidad de reinas atacandose (pares): ", first_queens)
        print("Solucion")

        start=time()
        max_states = 1000
        board_sol,number_states,truncated = simulated_annealing(board_cop,max_states)
        end=time()
        if truncated:
            board_sol.print_board()
            queens_sol=board_sol.objective_function()            
            print("El algoritmo fue truncado por alcanzar el maximo de estados")
            print("Cantidad de pares de reinas atacandose: ", queens_sol)
            print("cantidad de estados explorados: ", number_states )
            print("El algoritmo fue truncado por alcanzar el maximo de estados")
            guardar_resultados_csv(file,board_sol.n,"Simulated Annealing",truncated,number_states,end-start)
        else:
            board_sol.print_board()
            queens_sol=board_sol.objective_function()
            print("Cantidad de pares de reinas atacandose: ", queens_sol)
            print("cantidad de estados explorados: ", number_states)
            guardar_resultados_csv(file,board_sol.n,"Simulated Annealing",truncated,number_states,end-start)
        


    print("--------Genetic Algorithm------")

if __name__ == "__main__":
    seed("Hola soy la semilla ^^")
    with open('resultados.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(["N_Reinas","Algoritmo","Solucion","Explorados","Tiempo"])
        main()

