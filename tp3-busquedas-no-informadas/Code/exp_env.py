import gymnasium as gym
from gymnasium import wrappers

"""def generate_random_map_custom(
    size: int = 8, p: float = 0.8,seed: int = None):
    #Genera un mapa aleatorio para FrozenLake.
    return generate_random_map(size=size, p=p, seed=seed)"""

from gymnasium.envs.toy_text.frozen_lake import generate_random_map



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

               

