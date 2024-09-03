import pandas as pd
import matplotlib.pyplot as plt


# Cargar los datos desde los CSV
df = pd.read_csv(r'C:\Users\Enzo\Documents\UNCUYO\3-TERCERO\Inteligencia Artificial 1\ia-uncuyo-2024\tp4-busquedas-informadas\Code\resultados.csv')
df2 = pd.read_csv(r'C:\Users\Enzo\Documents\UNCUYO\3-TERCERO\Inteligencia Artificial 1\ia-uncuyo-2024\tp4-busquedas-informadas\Code\resultados_A_star.csv')

# Filtrar datos por nombre de algoritmo
A_data_1 = df2[df2['Algoritmo'] == 'A estrella E1']
A_data_2 = df2[df2['Algoritmo'] == 'A estrella E2']

uc_data_1 = df[df['Algoritmo'] == 'busqueda costo Uniforme E1']
uc_data_2 = df[df['Algoritmo'] == 'busqueda costo Uniforme E2']

# Crear los gráficos
plt.figure(figsize=(10, 6))
plt.boxplot([A_data_1['Estados Explorados'].dropna(), A_data_2['Estados Explorados'], uc_data_1['Estados Explorados'].dropna(), uc_data_2['Estados Explorados'].dropna()],
            labels=['A* E1', 'A* E2', 'UC1', 'UC2'])
plt.title('Comparativa de Estados Explorados')
plt.ylabel('Número de Estados Explorados')
plt.xlabel('Algoritmo')
plt.grid(True)
plt.savefig('comparativa_explorados.png')

plt.figure(figsize=(10, 6))
plt.boxplot([A_data_1['Tiempo de Ejecucion'].dropna(), A_data_2['Tiempo de Ejecucion'].dropna(), uc_data_1['Tiempo de Ejecucion'].dropna(), uc_data_2['Tiempo de Ejecucion'].dropna()],
            labels=['A* E1', 'A* E2', 'UC1', 'UC2'])

plt.title('Comparativa de Tiempos de Ejecución')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.xlabel('Algoritmo')
plt.grid(True)
plt.savefig('comparativa_tiempos.png')

plt.figure(figsize=(10, 6))
plt.boxplot([A_data_1['Costo del Camino'].dropna(), A_data_2['Costo del Camino'].dropna(), uc_data_1['Costo del Camino'].dropna(), uc_data_2['Costo del Camino'].dropna()],
            labels=['A* E1', 'A* E2', 'UC1', 'UC2'])
plt.title('Comparativa de Costos de Solución')
plt.ylabel('Costo de Solución')
plt.xlabel('Algoritmo')
plt.grid(True)
plt.savefig('comparativa_costos.png')

print("Costo de Solucion")

# Calcular promedio y desviación estándar

uc1_mean = uc_data_1['Costo del Camino'].mean()
uc1_std = uc_data_1['Costo del Camino'].std()

uc2_mean = uc_data_2['Costo del Camino'].mean()
uc2_std = uc_data_2['Costo del Camino'].std()

A1_mean = A_data_1['Costo del Camino'].mean()
A1_std = A_data_1['Costo del Camino'].std()

A2_mean = A_data_2['Costo del Camino'].mean()
A2_std = A_data_2['Costo del Camino'].std()


# Imprimir resultados
print(f"A* E1 - Promedio: {A1_mean}, Desviacion Estandar: {A1_std}")
print(f"A* E2 - Promedio: {A2_mean}, Desviacion Estandar: {A2_std}")
print(f"UC1 - Promedio: {uc1_mean}, Desviacion Estandar: {uc1_std}")
print(f"UC2 - Promedio: {uc2_mean}, Desviacion Estandar: {uc2_std}")


print("Estados Explorados")

uc1_mean = uc_data_1['Estados Explorados'].mean()
uc1_std = uc_data_1['Estados Explorados'].std()

uc2_mean = uc_data_2['Estados Explorados'].mean()
uc2_std = uc_data_2['Estados Explorados'].std()

A1_mean = A_data_1['Estados Explorados'].mean()
A1_std = A_data_1['Estados Explorados'].std()

A2_mean = A_data_2['Estados Explorados'].mean()
A2_std = A_data_2['Estados Explorados'].std()

# Imprimir resultados
print(f"A* E1 - Promedio: {A1_mean}, Desviacion Estandar: {A1_std}")
print(f"A* E2 - Promedio: {A2_mean}, Desviacion Estandar: {A2_std}")
print(f"UC1 - Promedio: {uc1_mean}, Desviacion Estandar: {uc1_std}")
print(f"UC2 - Promedio: {uc2_mean}, Desviacion Estandar: {uc2_std}")

print("Tiempo de Ejecución")

uc1_mean = uc_data_1['Tiempo de Ejecucion'].mean()
uc1_std = uc_data_1['Tiempo de Ejecucion'].std()

uc2_mean = uc_data_2['Tiempo de Ejecucion'].mean()
uc2_std = uc_data_2['Tiempo de Ejecucion'].std()

A1_mean = A_data_1['Tiempo de Ejecucion'].mean()
A1_std = A_data_1['Tiempo de Ejecucion'].std()

A2_mean = A_data_2['Tiempo de Ejecucion'].mean()
A2_std = A_data_2['Tiempo de Ejecucion'].std()

# Imprimir resultados
print(f"A* E1 - Promedio: {A1_mean}, Desviacion Estandar: {A1_std}")
print(f"A* E2 - Promedio: {A2_mean}, Desviacion Estandar: {A2_std}")
print(f"UC1 - Promedio: {uc1_mean}, Desviacion Estandar: {uc1_std}")
print(f"UC2 - Promedio: {uc2_mean}, Desviacion Estandar: {uc2_std}")
