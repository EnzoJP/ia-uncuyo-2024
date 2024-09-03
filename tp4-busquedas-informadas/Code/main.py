import gymnasium as gym
from gymnasium import wrappers
import time 
from A_star import *
from random import randint,seed
from utils import *
import csv

seed("hola soy la semilla ^^")

csv_name = 'resultados_A_star.csv'
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


    #Pruebas con los algoritmos de busqueda

    "--------------A * costo 1----------------"

    number_escenario=1
    print(f"Algoritmo A* E1")
    stoped=False

    for env in enviroments:
        success = False
        print(f"Escenario numero {number_escenario}\n")
        env.reset()
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

        result,explored,cost_actions = A_star_E1(map_description,start_position, goal_position)
        finish_time = time.time() - start_time

        if result is not None and len(result) <= nuevo_limite:
            # Reconstruir el camino de acciones para alcanzar la meta
            print(f"camino al objetivo:", result)
            if explored is not None:
                print(f"Estados explorados: {len(explored)}")
            print(f"Tiempo de ejecucion: {finish_time}\n")
            print(f"Costo del camino: {cost_actions}")

            #moves = execute_actions(env, result, start_position)
            success = True
            print("Goal found.")
        elif result is not None and len(result) > nuevo_limite:
            print("Goal found but the limit was reached.")
            stoped=True
            print(f"Tiempo de ejecucion: {finish_time}\n")
            #env.render()
        else:
            #env.render()
            print("Goal not found.")
            print(f"Tiempo de ejecucion: {finish_time}\n")

        guardar_resultados_csv(file,number_escenario, "A estrella E1", result, len(explored),finish_time,stoped,cost_actions)
        number_escenario+=1


    "--------------A * costo de acciones----------------"

    number_escenario=1
    print(f"Algoritmo A* E2")
    stoped=False

    for env in enviroments:
        success = False
        print(f"Escenario numero {number_escenario}\n")
        env.reset()
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

        result,explored,cost_actions = A_star_E2(map_description,start_position, goal_position)
        finish_time = time.time() - start_time

        if result is not None and len(result) <= nuevo_limite:
            # Reconstruir el camino de acciones para alcanzar la meta
            print(f"camino al objetivo:", result)
            if explored is not None:
                print(f"Estados explorados: {len(explored)}")
            print(f"Tiempo de ejecucion: {finish_time}\n")
            print(f"Costo del camino: {cost_actions}")

            #moves = execute_actions(env, result, start_position)
            success = True
            print("Goal found.")
        elif result is not None and len(result) > nuevo_limite:
            print("Goal found but the limit was reached.")
            stoped=True
            print(f"Tiempo de ejecucion: {finish_time}\n")
            #env.render()
        else:
            #env.render()
            print("Goal not found.")
            print(f"Tiempo de ejecucion: {finish_time}\n")

        guardar_resultados_csv(file,number_escenario, "A estrella E2", result, len(explored),finish_time,stoped,cost_actions)
        number_escenario+=1


