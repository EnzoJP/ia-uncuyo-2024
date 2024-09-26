import pandas as pd
import matplotlib.pyplot as plt


# Cargar los datos desde los CSV
df = pd.read_csv(r'C:\Users\Enzo\Documents\UNCUYO\3-TERCERO\Inteligencia Artificial 1\ia-uncuyo-2024\tp5-busquedas-locales\Code\resultados.csv')

# Filtrar datos por nombre de algoritmo
hill_data = df[df['Algoritmo'] == 'Hill Climbing']
sa_data = df[df['Algoritmo'] == 'Simulated Annealing']
gen_data = df[df['Algoritmo'] == 'Genetic Algorithm']

# Crear los gráficos
plt.figure(figsize=(10, 6))
plt.boxplot([hill_data['Explorados'].dropna(), sa_data['Explorados'].dropna(),],
            labels=['Hill Climbing', 'Simulated Annealing'])

plt.title('Comparativa de Estados Explorados')
plt.ylabel('Número de Estados Explorados')
plt.xlabel('Algoritmo')
plt.grid(True)
plt.savefig('comparativa_explorados.png')

plt.figure(figsize=(10, 6))
plt.boxplot([hill_data['Tiempo'].dropna(), sa_data['Tiempo'].dropna(), gen_data['Tiempo'].dropna()],
            labels=['Hill Climbing', 'Simulated Annealing', 'Genetico'])

plt.title('Comparativa de Tiempos de Ejecución')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.xlabel('Algoritmo')
plt.grid(True)
plt.savefig('comparativa_tiempos.png')

plt.figure(figsize=(10, 6))
plt.boxplot([hill_data['reinas_atacandose'].dropna(), sa_data['reinas_atacandose'].dropna(), gen_data['reinas_atacandose'].dropna()],
            labels=['Hill Climbing', 'Simulated Annealing', 'Genetico'])
plt.title('Comparativa de Cantidad de Reinas Atacandose')

plt.ylabel('Cantidad de Reinas Atacandose')
plt.xlabel('Algoritmo')
plt.grid(True)
plt.savefig('comparativa_reinas.png')

for size in df['N_Reinas'].unique():  # Iterar por cada tamaño de tablero
    # Filtrar datos por tamaño de tablero
    hill_size_data = hill_data[hill_data['N_Reinas'] == size]['reinas_atacandose'].dropna()
    sa_size_data = sa_data[sa_data['N_Reinas'] == size]['reinas_atacandose'].dropna()
    gen_size_data = gen_data[gen_data['N_Reinas'] == size]['reinas_atacandose'].dropna()
    
    # Crear boxplot
    plt.figure(figsize=(10, 6))
    plt.boxplot([hill_size_data, sa_size_data, gen_size_data],
                labels=['Hill Climbing', 'Simulated Annealing', 'Genetico'])
    
    # Etiquetas y título
    plt.title(f'Comparativa de Cantidad de Reinas Atacandose - Tamaño del Tablero: {size}')
    plt.ylabel('Cantidad de Reinas Atacandose')
    plt.xlabel('Algoritmo')
    plt.grid(True)
    
    # Guardar el gráfico
    plt.savefig(f'comparativa_reinas_tamaño_{size}.png')

# Calcular promedio y desviación estándar

hill_mean = hill_data['reinas_atacandose'].mean()
hill_std = hill_data['reinas_atacandose'].std()

sa_mean = sa_data['reinas_atacandose'].mean()
sa_std = sa_data['reinas_atacandose'].std()

gen_mean = gen_data['reinas_atacandose'].mean()
gen_std = gen_data['reinas_atacandose'].std()

# calcular el porcentaje de tableros resueltos
hill_optimal = hill_data[hill_data['Optima'] == True].count()
hill_optimal = hill_optimal['Optima']
hill_total = hill_data['Optima'].count()

sa_optimal = sa_data[sa_data['Optima'] == True].count()
sa_optimal = sa_optimal['Optima']
sa_total = sa_data['Optima'].count()

gen_optimal = gen_data[gen_data['Optima'] == True].count()
gen_optimal = gen_optimal['Optima']
gen_total = gen_data['Optima'].count()

hill_optimal = (hill_optimal/hill_total)*100
sa_optimal = (sa_optimal/sa_total)*100
gen_optimal = (gen_optimal/gen_total)*100

# Imprimir resultados
print(f"Hill Climbing - Promedio: {hill_mean}, Desviacion Estandar: {hill_std}, Porcentaje de tableros optimos: {hill_optimal}")
print(f"Simulated Annealing - Promedio: {sa_mean}, Desviacion Estandar: {sa_std}, Porcentaje de tableros optimos: {sa_optimal}")
print(f"Genetico - Promedio: {gen_mean}, Desviacion Estandar: {gen_std}, Porcentaje de tableros optimos: {gen_optimal}")

#calcular el porcentaje de tableros resueltos por tamaño

for size in df['N_Reinas'].unique():  # Iterar por cada tamaño de tablero
    # Filtrar datos por tamaño de tablero
    hill_size_data = hill_data[hill_data['N_Reinas'] == size]
    sa_size_data = sa_data[sa_data['N_Reinas'] == size]
    gen_size_data = gen_data[gen_data['N_Reinas'] == size]
    
    # calcular el porcentaje de tableros resueltos
    hill_optimal = hill_size_data[hill_size_data['Optima'] == True].count()
    hill_optimal = hill_optimal['Optima']
    hill_total = hill_size_data['Optima'].count()

    sa_optimal = sa_size_data[sa_size_data['Optima'] == True].count()
    sa_optimal = sa_optimal['Optima']
    sa_total = sa_size_data['Optima'].count()

    gen_optimal = gen_size_data[gen_size_data['Optima'] == True].count()
    gen_optimal = gen_optimal['Optima']
    gen_total = gen_size_data['Optima'].count()

    hill_optimal = (hill_optimal/hill_total)*100
    sa_optimal = (sa_optimal/sa_total)*100
    gen_optimal = (gen_optimal/gen_total)*100

    print(f"Tamano del tablero: {size}")
    print(f"Hill Climbing - Porcentaje de tableros optimos: {hill_optimal}")
    print(f"Simulated Annealing - Porcentaje de tableros optimos: {sa_optimal}")
    print(f"Genetico - Porcentaje de tableros optimos: {gen_optimal}")
    print("\n")

