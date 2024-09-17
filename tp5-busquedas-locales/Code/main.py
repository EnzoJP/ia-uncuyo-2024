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
            if queens_sol == 0:
                print("Solucion optima")
                optimal=True
            else:
                optimal=False
            print("cantidad de estados explorados: ", number_states )           
            guardar_resultados_csv(file,board_sol.n,"Hill Climbing",optimal,truncated,number_states,end-start,queens_sol)
        else:
            #board_sol.print_board()
            queens_sol=board_sol.objective_function()
            if queens_sol == 0:
                print("Solucion optima")
                optimal=True
            else:
                optimal=False
            print("Cantidad de pares de reinas atacandose: ", queens_sol)
            print("cantidad de estados explorados: ", number_states)
            guardar_resultados_csv(file,board_sol.n,"Hill Climbing",optimal,truncated,number_states,end-start,queens_sol)
        
    print("--------Simulated Annealing------")


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
        board_sol,number_states,truncated = simulated_annealing(board_cop,max_states)
        end=time()
        if truncated:
            #board_sol.print_board()
            queens_sol=board_sol.objective_function()            
            print("El algoritmo fue truncado por alcanzar el maximo de estados")
            print("Cantidad de pares de reinas atacandose: ", queens_sol)
            print("cantidad de estados explorados: ", number_states )
            if queens_sol == 0:
                print("Solucion optima")
                optimal=True
            else:
                optimal=False
            guardar_resultados_csv(file,board_sol.n,"Simulated Annealing",optimal,truncated,number_states,end-start,queens_sol)
        else:
            #board_sol.print_board()
            if queens_sol == 0:
                print("Solucion optima")
                optimal=True
            else:
                optimal=False
            queens_sol=board_sol.objective_function()
            print("Cantidad de pares de reinas atacandose: ", queens_sol)
            print("cantidad de estados explorados: ", number_states)
            guardar_resultados_csv(file,board_sol.n,"Simulated Annealing",optimal,truncated,number_states,end-start,queens_sol)
        


    print("--------Genetic Algorithm------")

    #voy a pasar por cada iteracion los 30 tableros de cada tamaño y van a hacer 30 it
    number=0
    four_quees_list = []
    eight_quees_list = []
    ten_quees_list = []
    for board in boards:
        board_cop = deepcopy(board) #copio para no modificar el original
        if number < 30:
            four_quees_list.append(board_cop)
        elif number < 60:
            eight_quees_list.append(board_cop)
        else:
            ten_quees_list.append(board_cop)
        number+=1


    for i in range(30):
        print("longitud del tablero: ", four_quees_list[i].n)
        #four_quees_list[i].print_board()
        print("Solucion")
        start=time()
        number_of_max_searches = 30
        board_sol,number_states = genetic_algorithm(four_quees_list,number_of_max_searches)
        end=time()
        queens_sol=board_sol.objective_function()
        if queens_sol == 0:
            print("Solucion optima")
            optimal=True
        else:
            optimal=False
        print("Cantidad de pares de reinas atacandose: ", queens_sol)
        print("cantidad de estados explorados: ", number_states)
        guardar_resultados_csv(file,board_sol.n,"Genetic Algorithm",optimal,False,number_states,end-start,queens_sol)

    for i in range(30):
        print("longitud del tablero: ", eight_quees_list[i].n)
        #eight_quees_list[i].print_board()
        print("Solucion")
        start=time()
        number_of_max_searches = 30
        board_sol,number_states = genetic_algorithm(eight_quees_list,number_of_max_searches)
        end=time()
        queens_sol=board_sol.objective_function()
        if queens_sol == 0:
            print("Solucion optima")
            optimal=True
        else:
            optimal=False
        print("Cantidad de pares de reinas atacandose: ", queens_sol)
        print("cantidad de estados explorados: ", number_states)
        guardar_resultados_csv(file,board_sol.n,"Genetic Algorithm",optimal,False,number_states,end-start,queens_sol)

    for i in range(30): 
        print("longitud del tablero: ", ten_quees_list[i].n)
        #ten_quees_list[i].print_board()
        print("Solucion")
        start=time()
        number_of_max_searches = 30
        board_sol,number_states = genetic_algorithm(ten_quees_list,number_of_max_searches)
        end=time()
        queens_sol=board_sol.objective_function()
        if queens_sol == 0:
            print("Solucion optima")
            optimal=True
        else:
            optimal=False
        print("Cantidad de pares de reinas atacandose: ", queens_sol)
        print("cantidad de estados explorados: ", number_states)
        guardar_resultados_csv(file,board_sol.n,"Genetic Algorithm",optimal,False,number_states,end-start,queens_sol)
        



if __name__ == "__main__":
    seed("Hola soy la semilla ^^")
    with open('resultados.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(["N_Reinas","Algoritmo","Optima","truncado?","Explorados","Tiempo","reinas_atacandose"])
        main()

