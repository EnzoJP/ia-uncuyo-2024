import gymnasium as gym
from gymnasium import wrappers
from random import randint,seed
from gymnasium.envs.toy_text.frozen_lake import generate_random_map


"""
nuevo_limite = 100
env = gym.make('FrozenLake-v1', render_mode='human').env
env = wrappers.TimeLimit(env, nuevo_limite)

print("Numero de estados:", env.observation_space.n)
print("Numero de acciones:", env.action_space.n)

state = env.reset()
print("Posicion inicial del agente:", state[0])
done = truncated = False

while not (done or truncated):
    action = env.action_space.sample() # Accion aleatoria
    next_state, reward, done, truncated, _ = env.step(action)
    print(f"Accion: {action}, Nuevo estado: {next_state}, Recompensa: {reward}")
    print(f"¿Gano? (encontro el objetivo): {done}")
    print(f"¿Freno? (alcanzo el maximo de pasos posible): {truncated}\n")
    state = next_state 
"""
               
def generate_random_map_custom(size,p,seed):
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
                    strin_map_custom[i][j] = 'H'  
                else:
                    strin_map_custom[i][j] = 'F'  

    desc = ["".join(row) for row in strin_map_custom]
    env = gym.make('FrozenLake-v1',desc=desc, render_mode='human').env
    return env

seed("1")
env=generate_random_map_custom(8,0.08,1)
env.reset()
env.render()