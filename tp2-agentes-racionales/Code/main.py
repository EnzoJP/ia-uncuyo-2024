from environment import *
from agent import *
from agent_random import *
from tabulate import tabulate
import copy

sizes = [2, 4, 8, 16, 32, 64, 128]  # 2x2, 4x4, 8x8, 16x16, 32x32, 64x64, 128x128
dirt_rates = [0.1, 0.2, 0.4, 0.8]   # 10%, 20%, 40%, 80%
repetitions = 10

results_reflexive = []
results_random = []

for size in sizes:
    for dirt_rate in dirt_rates:
        for i in range(repetitions):
            # Crear el entorno original
            env = Environment(size, size, 0, 0, dirt_rate)

            # Crear una copia del entorno para el agente aleatorio
            env_copy = copy.deepcopy(env)

            # agente reflexivo
            agent_reflexive = Agent(env)
            while agent_reflexive.get_battery() > 0:
                agent_reflexive.think(env)
            performance_reflexive = agent_reflexive.get_performance()
            battery_used_reflexive = agent_reflexive.get_battery_used()
            results_reflexive.append([size, dirt_rate, performance_reflexive, battery_used_reflexive])

            # agente aleatorio en la copia del entorno
            agent_random = AgentR(env_copy)
            while agent_random.get_battery() > 0:
                agent_random.think(env_copy)
            performance_random = agent_random.get_performance()
            battery_used_random = agent_random.get_battery_used()
            results_random.append([size, dirt_rate, performance_random, battery_used_random])

# Guardar resultados en archivos Md
headers = ["Size", "Dirt Rate", "Performance", "Battery Used"]

table_reflexive = tabulate(results_reflexive, headers, tablefmt="pipe")
with open("results_reflexive.md", "w") as f:
    f.write("# Resultados de la Simulación (Agente Reflexivo)\n\n")
    f.write(table_reflexive)

table_random = tabulate(results_random, headers, tablefmt="pipe")
with open("results_random.md", "w") as f:
    f.write("# Resultados de la Simulación (Agente Aleatorio)\n\n")
    f.write(table_random)

print("Resultados guardados en 'results_reflexive.md' y 'results_random.md'")




