#Problema de las 9 reinas con CSP

from board import Board
from random import randint,seed
from backtracking import BackTracking
from fowardCh import FowardChecking
from copy import deepcopy
from time import time
import csv
from utils import *
import matplotlib.pyplot as plt

def main():

    #creo los tableros y los guardo en una lista 30 por cada tamaño
    sizes = [4,8,10,12,15]
    boards = []
    iterations = 30
    for size in sizes:
        for i in range(iterations):
            #creo un tablero
            board = Board(size)
            #board.random_board()
            boards.append(board)

    #probamos los algoritmos en los tableros creados
    print("-------Backtracking------")

    for board in boards:
        board_cop = deepcopy(board) #copio para no modificar el original
        print("Numero de tablero: ", boards.index(board)+1)
        print("longitud del tablero: ", board.n)
        #board.print_board()
        print("Solucion")
        
        start=time()
        max_states = 10000
        result,truncated,board_sol,number_states = BackTracking(board_cop,max_states)
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
            guardar_resultados_csv(file,board_sol.n,"BackTracking",optimal,truncated,number_states,end-start,queens_sol)
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
            guardar_resultados_csv(file,board_sol.n,"BackTracking",optimal,truncated,number_states,end-start,queens_sol)
        
    print("--------foward checking------")

    for board in boards:
        board_cop = deepcopy(board) #copio para no modificar el original
        print("Numero de tablero: ", boards.index(board)+1)
        print("longitud del tablero: ", board.n)
        #board.print_board()
        print("Solucion")

        start=time()
        max_states = 10000
        nstates=0
        _,truncated,board_sol,number_states = FowardChecking(board_cop,max_states)
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
            guardar_resultados_csv(file,board_sol.n,"FowardChecking",optimal,truncated,number_states,end-start,queens_sol)
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
            guardar_resultados_csv(file,board_sol.n,"FowardChecking",optimal,truncated,number_states,end-start,queens_sol)
        

if __name__ == "__main__":
    seed("Hola soy la semilla ^^")
    with open('resultados.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(["N_Reinas","Algoritmo","Optima","truncado?","Explorados","Tiempo","reinas_atacandose"])
        main()

