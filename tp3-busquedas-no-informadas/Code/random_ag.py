import gymnasium as gym
from gymnasium import wrappers
import time 
from searches import *
from random import randint,seed
from utils import *
from searches import get_neighbors
import csv

def random_path(grid,start,goal):
    frontier = [(start, [])]  # (posición actual, camino tomado)
    explored = set()
    it_max=1000
    
    while frontier:
        if len(explored) >= it_max:
            return None,explored
        position, path = frontier.pop()

        explored.add(position)

        if grid[position[0]][position[1]] == b'G':  # Llegamos al objetivo
                return path + [position],explored
        
        neighbors = get_neighbors(position, grid)
        for neighbor in neighbors:
            action_Random=randint(0,len(neighbors)-1)
            neighboral = neighbors[action_Random]
            if grid[neighbor[0]][neighbor[1]] != b'H':
                frontier.append((neighboral, path + [position]))
                break
            

    return None,explored  # Si no se encuentra el objetivo

seed("hola soy la semilla ^^")

csv_name = 'resultados_Random.csv'
with open(csv_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Escenario', 'Algoritmo', 'Alcanzo el resultado', 'Estados Explorados', 'Tiempo de Ejecución','Alcanzo el limite', 'Costo del Camino'])

    #Crear los entornos de gym con mapas aleatorios y guardarlos en una lista
    iterations = 30
    enviroments = []

    for i in range(iterations):
        
        env = generate_random_map_custom(100,(1-0.08))
        #modificamos el limite de pasos a 1000
        nuevo_limite = 1000
        env = wrappers.TimeLimit(env, nuevo_limite)
        enviroments.append(env)


    "-------el agente elige las acciones al azar----------"


    print(f"nombre: agente aleatorio")
    number_escenario=1

    for env in enviroments:

        print(f"Iteracion {number_escenario}")
        state = env.reset()

        start_time = time.time()

        # Acceder a la descripción del mapa
        map_description = env.unwrapped.desc

        start_position = None
        goal_position = None

        for i in range(len(map_description)):
            for j in range(len(map_description[i])):
                if map_description[i][j] == b'S':  # la 'b' para bytes en Gymnasium
                    start_position = (i, j)
                elif map_description[i][j] == b'G':
                    goal_position = (i, j)

        result,explored = random_path(map_description,start_position, goal_position)

        finish_time = time.time() - start_time

        done = env.unwrapped


        if result is not None and len(result) <= nuevo_limite:
            # Reconstruir el camino de acciones para alcanzar la meta
            print(f"camino al objetivo:", result)
            if explored is not None:
                print(f"Estados explorados: {len(explored)}")
            print(f"Tiempo de ejecucion: {finish_time}\n")

            #moves = execute_actions(env, result, start_position)
            success = True
            print("Goal found.")
        elif result is not None and len(result) > nuevo_limite:
            print("Goal found but the limit was reached.")
            print(f"Tiempo de ejecucion: {finish_time}\n")
            #env.render()
        else:
            #env.render()
            print("Goal not found.")
            print(f"Tiempo de ejecucion: {finish_time}\n")

        guardar_resultados_csv(file,number_escenario, "Random", result, len(explored), finish_time, False, len(result) if result is not None else None)
        number_escenario+=1