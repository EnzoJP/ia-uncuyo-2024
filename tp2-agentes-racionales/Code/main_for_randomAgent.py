from environment import *
from agent_random import *
from tabulate import tabulate

sizes = [2,4,8,16,32,64,128]  # 2x2, 4x4, 8x8, 16x16, 32x32, 64x64, 128x128
dirt_rates = [0.1,0.2,0.4,0.8] # 10%, 20%, 40%, 80%
repetitions = 10

results = []

for size in sizes:
    for dirt_rate in dirt_rates:
        for i in range(repetitions):
            env = Environment(size, size, 0, 0, dirt_rate)
            agent = AgentR(env)
            env.print_environment()
            while agent.get_battery() > 0:
                agent.think(env)
            print("Size: ", size, "Dirt rate: ", dirt_rate, "Performance: ", agent.get_performance())
            print("life or battery used: ", agent.get_battery_used())
            performance = agent.get_performance()
            battery_used = agent.get_battery_used()
            results.append([size, dirt_rate, performance, battery_used])


headers = ["Size", "Dirt Rate", "Performance", "Battery Used"]
table = tabulate(results, headers, tablefmt="pipe")


with open("results_randomAgent.md", "w") as f:
    f.write("# Resultados de la Simulación\n\n")
    f.write(table)

print("Resultados guardados en 'results.md'")