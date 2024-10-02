import pandas as pd
import matplotlib.pyplot as plt


# Cargar los datos desde los CSV
df = pd.read_csv(r'C:\Users\Enzo\Documents\UNCUYO\3-TERCERO\Inteligencia Artificial 1\ia-uncuyo-2024\tp6-csp\Code\resultados.csv')

# Filtrar datos por nombre de algoritmo
bc_data = df[df['Algoritmo'] == 'BackTracking']
fc_data = df[df['Algoritmo'] == 'FowardChecking']


# Crear los gráficos
plt.figure(figsize=(10, 6))
plt.boxplot([bc_data['Explorados'].dropna(), fc_data['Explorados'].dropna(),],
            labels=['BackTracking', 'FowardChecking'])

plt.title('Comparativa de Estados Explorados')
plt.ylabel('Número de Estados Explorados')
plt.xlabel('Algoritmo')
plt.grid(True)
plt.savefig('comparativa_explorados.png')

plt.figure(figsize=(10, 6))
plt.boxplot([bc_data['Tiempo'].dropna(), fc_data['Tiempo'].dropna()],
            labels=['BackTracking', 'FowardChecking'])

plt.title('Comparativa de Tiempos de Ejecución')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.xlabel('Algoritmo')
plt.grid(True)
plt.savefig('comparativa_tiempos.png')

plt.figure(figsize=(10, 6))
plt.boxplot([bc_data['reinas_atacandose'].dropna(), fc_data['reinas_atacandose'].dropna(),],
            labels=['BackTracking', 'FowardChecking'])
plt.title('Comparativa de Cantidad de Reinas Atacandose')

plt.ylabel('Cantidad de Reinas Atacandose')
plt.xlabel('Algoritmo')
plt.grid(True)
plt.savefig('comparativa_reinas.png')

import numpy as np

for size in df['N_Reinas'].unique():  # Iterar por cada tamaño de tablero
    # Filtrar datos por tamaño de tablero
    b = bc_data[bc_data['N_Reinas'] == size]['Explorados'].dropna()
    f = fc_data[fc_data['N_Reinas'] == size]['Explorados'].dropna()
    
    b_mean = b.mean() if not b.empty else 0
    f_mean = f.mean() if not f.empty else 0
    b_std = b.std() if not b.empty else 0
    f_std = f.std() if not f.empty else 0

    # Crear gráfico de barras
    bar_width = 0.35
    x = np.arange(2)  # Dos grupos: BackTracking y FowardChecking
    means = [b_mean, f_mean]
    stds = [b_std, f_std]

    plt.figure(figsize=(10, 6))
    plt.bar(x, means, width=bar_width, yerr=stds, capsize=5, color=['blue', 'orange'], alpha=0.7)

    # Etiquetas y título
    plt.title(f'Comparativa de explorados - Tamaño del Tablero: {size}')
    plt.ylabel('Explorados')
    plt.xlabel('Algoritmo')
    plt.xticks(x, ['BackTracking', 'FowardChecking'])  # Etiquetas de los grupos
    plt.grid(axis='y')
    
    # Guardar el gráfico
    plt.savefig(f'comparativa_reinas_explorados_{size}.png')
    plt.close()  # Cerrar la figura para liberar memoria


# Calcular promedio y desviación estándar

fc = fc_data['Explorados'].mean()
fc_std = fc_data['Explorados'].std()

bc = bc_data['Explorados'].mean()
bc_std = bc_data['Explorados'].std()

print(f'FowardChecking - Promedio: {fc}, Desviación Estándar: {fc_std}')
print(f'BackTracking - Promedio: {bc}, Desviación Estándar: {bc_std}')
