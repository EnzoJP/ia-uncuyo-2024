import pandas as pd
import matplotlib.pyplot as plt


# Cargar los datos desde los CSV
df = pd.read_csv(r'C:\Users\Enzo\Documents\UNCUYO\3-TERCERO\Inteligencia Artificial 1\ia-uncuyo-2024\tp3-busquedas-no-informadas\Code\resultados.csv')


# Filtrar datos por nombre de algoritmo
bfs_data = df[df['Algoritmo'] == 'busqueda en amplitud']
dfs_data = df[df['Algoritmo'] == 'busqueda en profundidad']
dfs_data_l = df[df['Algoritmo'] == 'busqueda en profundidad limitada']
uc_data_1 = df[df['Algoritmo'] == 'busqueda costo Uniforme E1']
uc_data_2 = df[df['Algoritmo'] == 'busqueda costo Uniforme E2']

# Crear los gráficos
plt.figure(figsize=(10, 5))
plt.boxplot([bfs_data['Estados Explorados'].dropna(), dfs_data['Estados Explorados'], uc_data_1['Estados Explorados'].dropna(), uc_data_2['Estados Explorados'].dropna()],
            labels=['BFS', 'DFS and Dfs limited', 'UC1', 'UC2'])
plt.title('Comparativa de Estados Explorados')
plt.ylabel('Número de Estados Explorados')
plt.xlabel('Algoritmo')
plt.grid(True)
plt.savefig('comparativa_explorados.png')

plt.figure(figsize=(10, 6))
plt.boxplot([bfs_data['Tiempo de Ejecucion'].dropna(), dfs_data['Tiempo de Ejecucion'].dropna(), dfs_data_l['Tiempo de Ejecucion'].dropna(), uc_data_1['Tiempo de Ejecucion'].dropna(), uc_data_2['Tiempo de Ejecucion'].dropna()],
            labels=['BFS', 'DFS', 'DFS Limitada', 'UC1', 'UC2'])
plt.title('Comparativa de Tiempos de Ejecución')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.xlabel('Algoritmo')
plt.grid(True)
plt.savefig('comparativa_tiempos.png') 

#costos
plt.figure(figsize=(10, 6))
plt.boxplot([uc_data_1['Costo del Camino'].dropna(), uc_data_2['Costo del Camino'].dropna()],label=['UC1', 'UC2'])
plt.title('Comparativa de Costos de Solución')
plt.ylabel('Costo de Solución')
plt.xlabel('Algoritmo')
plt.grid(True)
plt.savefig('comparativa_costos.png')


df = pd.read_csv(r'C:\Users\Enzo\Documents\UNCUYO\3-TERCERO\Inteligencia Artificial 1\ia-uncuyo-2024\tp3-busquedas-no-informadas\Code\resultados_Random.csv')

# Filtrar datos por nombre de algoritmo
data = df[df['Algoritmo'] == 'Random']

# Crear los gráficos
plt.figure(figsize=(10, 10))
plt.boxplot([data['Estados Explorados'].dropna()],
            labels=['Random'])
plt.title('Estados Explorados')
plt.ylabel('Número de Estados Explorados')
plt.xlabel('Algoritmo')
plt.grid(True)
plt.savefig('explorados_random.png')


plt.figure(figsize=(10, 10))
plt.boxplot([data['Tiempo de Ejecucion'].dropna()],
            labels=['Random'])
plt.title('Tiempo de Ejecución')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.xlabel('Algoritmo')
plt.grid(True)

plt.savefig('tiempos_random.png')


print("Estados Explorados")

bfs_mean = bfs_data['Estados Explorados'].mean()
bfs_std = bfs_data['Estados Explorados'].std()

dfs_mean = dfs_data['Estados Explorados'].mean()
dfs_std = dfs_data['Estados Explorados'].std()

dfs_l_mean = dfs_data_l['Estados Explorados'].mean()
dfs_l_std = dfs_data_l['Estados Explorados'].std()

uc1_mean = uc_data_1['Estados Explorados'].mean()
uc1_std = uc_data_1['Estados Explorados'].std()

uc2_mean = uc_data_2['Estados Explorados'].mean()
uc2_std = uc_data_2['Estados Explorados'].std()

# Imprimir resultados
print(f"BFS - Promedio: {bfs_mean}, Desviacion Estandar: {bfs_std}")
print(f"DFS - Promedio: {dfs_mean}, Desviacion Estandar: {dfs_std}")
print(f"DFS Limitada - Promedio: {dfs_l_mean}, Desviación Estandar: {dfs_l_std}")
print(f"UC1 - Promedio: {uc1_mean}, Desviacion Estandar: {uc1_std}")
print(f"UC2 - Promedio: {uc2_mean}, Desviacion Estandar: {uc2_std}")

print("Tiempo de Ejecución")

bfs_mean = bfs_data['Tiempo de Ejecucion'].mean()
bfs_std = bfs_data['Tiempo de Ejecucion'].std()

dfs_mean = dfs_data['Tiempo de Ejecucion'].mean()
dfs_std = dfs_data['Tiempo de Ejecucion'].std()

dfs_l_mean = dfs_data_l['Tiempo de Ejecucion'].mean()
dfs_l_std = dfs_data_l['Tiempo de Ejecucion'].std()

uc1_mean = uc_data_1['Tiempo de Ejecucion'].mean()
uc1_std = uc_data_1['Tiempo de Ejecucion'].std()

uc2_mean = uc_data_2['Tiempo de Ejecucion'].mean()
uc2_std = uc_data_2['Tiempo de Ejecucion'].std()

# Imprimir resultados
print(f"BFS - Promedio: {bfs_mean}, Desviacion Estandar: {bfs_std}")
print(f"DFS - Promedio: {dfs_mean}, Desviacion Estandar: {dfs_std}")
print(f"DFS Limitada - Promedio: {dfs_l_mean}, Desviación Estandar: {dfs_l_std}")
print(f"UC1 - Promedio: {uc1_mean}, Desviacion Estándar: {uc1_std}")
print(f"UC2 - Promedio: {uc2_mean}, Desviacion Estándar: {uc2_std}")

print("Costo de Solucion")

bfs_mean = bfs_data['Costo del Camino'].mean()
bfs_std = bfs_data['Costo del Camino'].std()

dfs_mean = dfs_data['Costo del Camino'].mean()
dfs_std = dfs_data['Costo del Camino'].std()

dfs_l_mean = dfs_data_l['Costo del Camino'].mean()
dfs_l_std = dfs_data_l['Costo del Camino'].std()

uc1_mean = uc_data_1['Costo del Camino'].mean()
uc1_std = uc_data_1['Costo del Camino'].std()

uc2_mean = uc_data_2['Costo del Camino'].mean()
uc2_std = uc_data_2['Costo del Camino'].std()

# Imprimir resultados
print(f"BFS - Promedio: {bfs_mean}, Desviacion Estandar: {bfs_std}")
print(f"DFS - Promedio: {dfs_mean}, Desviacion Estandar: {dfs_std}")
print(f"DFS Limitada - Promedio: {dfs_l_mean}, Desviacion Estándar: {dfs_l_std}")
print(f"UC1 - Promedio: {uc1_mean}, Desviacion Estandar: {uc1_std}")
print(f"UC2 - Promedio: {uc2_mean}, Desviacion Estandar: {uc2_std}")












