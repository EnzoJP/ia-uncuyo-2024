from gymnasium.envs.toy_text.frozen_lake import generate_random_map
import gymnasium as gym
from A_star import *
from random import randint
import csv


def generate_random_map_custom(size,p):
    #posiciones de inicio y fin
    start_pos_row=randint(0,size-1)
    start_pos_col=randint(0,size-1)

    goal_pos_row=randint(0,size-1)
    goal_pos_col=randint(0,size-1)
    
    while start_pos_row==goal_pos_row and start_pos_col==goal_pos_col:
        goal_pos_row=randint(0,size-1)
        goal_pos_row=randint(0,size-1)

    #generar mapa
    strin_map_custom = []
    for i in range(size):
        fila = []
        for j in range(size):
            fila.append('') 
        strin_map_custom.append(fila)
        
    for i in range(size):
        for j in range(size):
            if i == start_pos_row and j == start_pos_col:
                strin_map_custom[i][j] = 'S'  
            elif i == goal_pos_row and j == goal_pos_col:
                strin_map_custom[i][j] = 'G' 
            else:
                if randint(0, 100) < p * 100:
                    strin_map_custom[i][j] = 'F'  
                else:
                    strin_map_custom[i][j] = 'H'  

    desc = ["".join(row) for row in strin_map_custom]
    env = gym.make('FrozenLake-v1',desc=desc, render_mode='human',is_slippery=False)
    return env

def execute_actions(env, path, start_position):

    if path is None or len(path) < 2:
        print("No se puede ejecutar porque no se encontró un camino válido.")
        return env
    state = env.reset()
    current_position = start_position

    for next_position in path[1:]:  # Saltar la posición inicial
        x1, y1 = current_position
        x2, y2 = next_position
        if x1 == x2 and y1 < y2:
            action = 2  # Derecha
        elif x1 == x2 and y1 > y2:
            action = 0  # Izquierda
        elif y1 == y2 and x1 < x2:
            action = 1  # Abajo
        elif y1 == y2 and x1 > x2:
            action = 3  # Arriba

        next_state, _, done, truncated, _ = env.step(action)
        if done or truncated:
            break
        current_position = next_position

    return env




# Añadir resultados al CSV en cada iteración
def guardar_resultados_csv(file,number_escenario, algoritmo, result, explored, finish_time,stoped, cost_of_actions=None):
        writer = csv.writer(file)
        writer.writerow([number_escenario, algoritmo, True if result is not None and stoped==False else 'N/A', explored if explored is not None and stoped==False else 'N/A', finish_time,stoped, cost_of_actions])