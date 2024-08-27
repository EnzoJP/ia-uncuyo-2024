from gymnasium.envs.toy_text.frozen_lake import generate_random_map
import gymnasium as gym
from gymnasium import wrappers
import time 
from searches import *

#1) Crear los entornos de gym con mapas aleatorios y guardarlos en una lista
iterations = 30
enviroments = []

for i in range(iterations):
    #creamos 30 mapas aleatorios con semillas de 1 a 30
    print(f"Iteracion {i}")
    
    env = gym.make('FrozenLake-v1',desc = generate_random_map(size=100, p=0.8, seed=i), render_mode='human')
    #modificamos el limite de pasos a 1000
    nuevo_limite = 1000
    env = wrappers.TimeLimit(env, nuevo_limite)
    print("Numero de estados:", env.observation_space.n)
    print("Numero de acciones:", env.action_space.n)    
    start_state = env.reset()
    print("Posicion inicial del agente:", start_state[0])

    enviroments.append(env) #guardamos el entorno en la lista


"--------------busqueda en amplitud----------------"
iterations = 30

for it in range(iterations):

    print(f"Iteracion {it}")
    print(f"nombre: busqueda en amplitud")
    for env in enviroments:

        start_time = time.time()
        st=env.reset()
        result,explored = Searches.breadth_first_search(env,st[0], env.observation_space.n - 1)
        finish_time = time.time() - start_time
        
        if result is not None:
            # Reconstruir el camino de acciones para alcanzar la meta
            path = []
            while result:
                if result.action is not None:
                    path.append(result.action)
                result = result.parent
            path.reverse()
            print(f"semilla: {i}")
            print(f"camino al objetivo:", path)
            if explored is not None:
                print(f"Estados explorados: {len(explored)}")
            print(f"Tiempo de ejecucion: {finish_time}\n")
            
        else:
            print(f"semilla: {i}")
            print("Goal not found.")
            print(f"Tiempo de ejecucion: {finish_time}\n")




"----------busqueda en profundidad----------------"
iterations = 30

for it in range(iterations):
    
    print(f"Iteracion {it}")
    print(f"nombre: busqueda en profundidad")
    for env in enviroments:

        start_time = time.time()
        result,explored = Searches.depth_first_search(env,st[0], env.observation_space.n - 1)
        finish_time = time.time() - start_time
        
        if result is not None:
            # Reconstruir el camino de acciones para alcanzar la meta
            path = []
            while result:
                if result.action is not None:
                    path.append(result.action)
                result = result.parent
            path.reverse()
            print(f"semilla: {i}")
            print(f"camino al objetivo:", path)
            print(f"Estados explorados: {len(explored)}")
            print(f"Tiempo de ejecucion: {finish_time}\n")
            
        else:
            print("Goal not found.")


"------------busqueda en profundidad limitada----------------"
iterations = 30

for it in range(iterations):
    
    print(f"Iteracion {it}")
    print(f"nombre: busqueda en profundidad limitada")
    for env in enviroments:

        start_time = time.time()
        limit=500
        result,explored = Searches.limited_dfs(env,st[0], env.observation_space.n - 1,limit)
        finish_time = time.time() - start_time
        
        if result is not None:
            # Reconstruir el camino de acciones para alcanzar la meta
            path = []
            while result:
                if result.action is not None:
                    path.append(result.action)
                result = result.parent
            path.reverse()
            print(f"semilla: {i}")
            print(f"camino al objetivo:", path)
            print(f"Estados explorados: {len(explored)}")
            print(f"Tiempo de ejecucion: {finish_time}\n")
            
        else:
            print("Goal not found.")


"-----------Busqueda costo uniforme----------------"

#Escenario 1: Cada accion tiene costo 1

iterations = 30


#Escenario 2: Las acciones tienen como costo asociado el numero entero que representa a la
#accion, es decir, moverse a la izquierda no tiene costo, moverse hacia abajo tiene costo 1,etc.

iterations = 30


"5) -------el agente elige las acciones al azar----------"

iterations = 30
for i in range(iterations):
    print(f"Iteracion {i}")
    start_time = time.time()
    state = env.reset()
    done = truncated = False
    total_reward = 0
    states_visited = []
    while not (done or truncated):
        action = env.action_space.sample() # Accion aleatoria
        next_state, reward, done, truncated, _ = env.step(action)
        total_reward += reward
        state = next_state
        if state not in states_visited:
            states_visited.append(state)
    finish_time = time.time() - start_time
    print(f"nombre: agente aleatorio")
    print(f"semilla: {i}")
    print(f"Recompensa total: {total_reward}")
    print(f"¿Gano? (encontro el objetivo): {done}")
    print(f"¿Freno? (alcanzo el maximo de pasos posible): {truncated}\n")
    print(f"Estados visitados: {len(states_visited)}\n")
    print(f"Tiempo de ejecucion: {finish_time}\n")


    



